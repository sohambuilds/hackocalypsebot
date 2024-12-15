import streamlit as st
from RagAnswerGenerator import RagAnswerGenerator
import os
import tempfile

# Initialize the RAG Answer Generator
def init_rag(uploaded_file):
    if not uploaded_file:
        st.error("Error: No file uploaded.")
        return None
    
    # Create a temporary directory to save the uploaded file
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Save the uploaded file to the temporary directory
        file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Initialize the RagAnswerGenerator with the temporary directory containing the uploaded file
        return RagAnswerGenerator(temp_dir)
    except Exception as e:
        st.error(f"Error saving file: {e}")
        return None

# Streamlit App
def main():
    st.set_page_config(
        page_title="RAG Chat System",
        page_icon="🗺️",
        layout="wide"
    )

    st.title("🗺️ RAG Chat System")
    st.write("Ask questions about the maps or related documents in the uploaded file.")
    
    # File upload
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    if 'rag' not in st.session_state:
        st.session_state.rag = None
    
    # Initialize the RAG system after file upload
    if uploaded_file and st.button("Initialize RAG System"):
        st.session_state.rag = init_rag(uploaded_file)
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
