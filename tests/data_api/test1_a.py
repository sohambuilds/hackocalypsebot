import numpy as np
import requests
from transformers import BertTokenizer, BertModel
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity

# Define API URLs and headers
GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MONSTER_API_URL = "https://api.mlsakiit.com/monsters"
SURVIVORS_API_URL = "https://api.mlsakiit.com/survivors"
RESOURCES_API_URL = "https://api.mlsakiit.com/resources"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

# Load a BERT model and tokenizer for embedding using Hugging Face (without torch)
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Function to fetch data from an API
def fetch_data(api_url, error_message, default_response):
    try:
        response = requests.get(api_url, headers={"accept": "application/json"})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"{error_message}: {e}")
        return default_response

# Fetch monster, resource, and survivor data
def fetch_monster_data():
    return fetch_data(MONSTER_API_URL, "Error fetching monster data", [{"monster_id": "unknown", "lat": 0, "lon": 0}])

def fetch_resource_data():
    return fetch_data(RESOURCES_API_URL, "Error fetching resource data", [])

def fetch_survivor_data():
    return fetch_data(SURVIVORS_API_URL, "Error fetching survivor data", [])

# Format data into readable context
def format_monster_data(monsters):
    formatted = []
    for monster in monsters:
        if isinstance(monster, dict):
            monster_id = monster.get("monster_id", "unknown")
            lat = monster.get("lat", "unknown")
            lon = monster.get("lon", "unknown")
            formatted.append(f"Monster {monster_id} at ({lat}, {lon})")
        else:
            formatted.append("Invalid monster data")
    return formatted

def format_survivor_data(survivors):
    formatted = []
    for survivor in survivors:
        if isinstance(survivor, dict):
            survivor_id = survivor.get("survivor_id", "unknown")
            district = survivor.get("district", "unknown")
            lat = survivor.get("lat", "unknown")
            lon = survivor.get("lon", "unknown")
            formatted.append(f"Survivor {survivor_id} in {district} ({lat}, {lon})")
        else:
            formatted.append("Invalid survivor data")
    return formatted

def format_resource_data(resources):
    formatted = []
    for resource in resources:
        if isinstance(resource, dict):
            props = resource.get("properties", {})
            dist_name = props.get("dist_name", "Unknown")
            temp = props.get("temp", "N/A")
            food = props.get("food_rations", "N/A")
            formatted.append(f"{dist_name}: Temp {temp}\u00b0C, Food {food}kg")
        else:
            formatted.append("Invalid resource data")
    return formatted

# Generate embeddings for texts using Hugging Face's transformers
def get_embeddings(texts):
    try:
        inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt", max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
            embeddings = outputs.last_hidden_state
            return torch.mean(embeddings, dim=1).numpy()  # Mean pooling
    except Exception as e:
        st.error(f"Error generating embeddings: {e}")
        return np.zeros((len(texts), 768))  # Return zero embeddings as fallback

# Calculate cosine similarity
def calculate_cosine_similarity(query_embedding, context_embeddings):
    return cosine_similarity(query_embedding, context_embeddings)

# Find the most relevant context based on cosine similarity
def find_relevant_context(query, context):
    try:
        query_embedding = get_embeddings([query])
        context_embeddings = get_embeddings(context)
        similarities = calculate_cosine_similarity(query_embedding, context_embeddings)
        top_indices = np.argsort(similarities[0])[::-1]
        return [context[i] for i in top_indices[:3]]  # Top 3 relevant contexts
    except Exception as e:
        st.error(f"Error finding relevant context: {e}")
        return []

# Generate a response using Groq API
def generate_response(query, context):
    messages = [{"role": "user", "content": query}] + [{"role": "system", "content": doc} for doc in context]
    try:
        response = requests.post(GROQ_API_URL, json={
            "model": "mixtral-8x7b-32768",
            "messages": messages
        }, headers=HEADERS)
        response.raise_for_status()
        response_data = response.json()
        return response_data.get("choices", [{}])[0].get("message", {}).get("content", "No response available.")
    except Exception as e:
        return f"Error generating response: {e}"

# Main function to run the chatbot on Streamlit
def run_chatbot():
    monsters = fetch_monster_data()
    survivors = fetch_survivor_data()
    resources = fetch_resource_data()

    context = format_monster_data(monsters)
    context += format_survivor_data(survivors)
    context += format_resource_data(resources)

    st.title("Survival Chatbot")
    st.write("Ask me anything about survival!")

    query = st.text_input("Your question:")
    if query:
        relevant_context = find_relevant_context(query, context)
        response = generate_response(query, relevant_context)
        st.write("Chatbot Response:")
        st.write(response)

# Run the Streamlit app
if __name__ == "__main__":
    run_chatbot()
