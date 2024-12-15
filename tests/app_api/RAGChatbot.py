import streamlit as st
import faiss
from DataFetcher import DataFetcher
from DataFormatter import DataFormatter
from Embedder import Embedder
from GroqAPI import GroqAPI

# 5. RAGChatbot Class
class RAGChatbot:
    def __init__(self):
        self.data_fetcher = DataFetcher()
        self.data_formatter = DataFormatter()
        self.embedder = Embedder()
        self.groq_api = GroqAPI()

    def search_relevant_context(self, query, context):
        # Get embeddings for the context and the query
        context_embeddings = self.embedder.get_embeddings(context)
        query_embedding = self.embedder.get_embeddings([query])

        # Create FAISS index
        index = faiss.IndexFlatL2(context_embeddings.shape[1])  # Using L2 distance (Euclidean)
        index.add(context_embeddings)

        # Search for the most similar context
        _, indices = index.search(query_embedding, k=3)  # Retrieve top 3 similar contexts
        relevant_context = [context[i] for i in indices[0]]

        return relevant_context

    def generate_response(self, query):
        # Step 1: Fetch monster, survivor, and resource data from APIs
        monsters = self.data_fetcher.fetch_monster_data()
        survivors = self.data_fetcher.fetch_survivor_data()
        resources = self.data_fetcher.fetch_resource_data()

        # Step 2: Format the data into readable context
        context = self.data_formatter.format_monster_data(monsters)
        context += self.data_formatter.format_survivor_data(survivors)
        context += self.data_formatter.format_resource_data(resources)

        # Step 3: Use FAISS to retrieve relevant context
        relevant_context = self.search_relevant_context(query, context)

        # Step 4: Generate a response based on the query and retrieved context
        response = self.groq_api.generate_response(query, relevant_context)

        return response

# Streamlit UI
st.title("RAG Chatbot for Survival Assistance")
st.write("Ask me anything about surviving in this world!")

# Initialize chatbot
chatbot = RAGChatbot()

# Create a chat history list for the conversation
if 'history' not in st.session_state:
    st.session_state.history = []

# Input field for user query
query = st.text_input("Your question:", "")

if query:
    # Add the user query to the history
    st.session_state.history.append(f"User: {query}")

    # Get the chatbot's response
    response = chatbot.generate_response(query)

    # Add the chatbot's response to the history
    st.session_state.history.append(f"Chatbot: {response}")

# Display chat history
for message in st.session_state.history:
    st.write(message)
