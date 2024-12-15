import streamlit as st
from RagAnswerGenerator import RagAnswerGenerator
import os

# Initialize the RAG Answer Generator
def init_rag(directory):
    if not os.path.exists(directory):
        st.error(f"Error: The specified directory '{directory}' does not exist.")
        return None
    return RagAnswerGenerator(directory)

# Streamlit App
def main():
    st.set_page_config(
        page_title="RAG Chat System",
        page_icon="🗺️",
        layout="wide"
    )

    st.title("🗺️ RAG Chat System")
    st.write("Ask questions about the maps or related documents in the specified directory.")
    
    # Directory input
    directory = st.text_input("Enter the directory containing text files:", value="/content")
    if 'rag' not in st.session_state:
        st.session_state.rag = None
    
    # Initialize the RAG system
    if st.button("Initialize RAG System"):
        st.session_state.rag = init_rag(directory)
        if st.session_state.rag:
            st.success("RAG System initialized successfully!")

    # Chat system
    if st.session_state.rag:
        user_question = st.text_input("Ask your question:")
        if st.button("Get Answer"):
            if user_question.strip():
                try:
                    answer = st.session_state.rag.generate_answer(user_question)
                    st.write("### Response:")
                    st.success(answer)
                except Exception as e:
                    st.error(f"Error generating answer: {e}")
            else:
                st.warning("Please enter a valid question.")

if __name__ == "__main__":
    main()
