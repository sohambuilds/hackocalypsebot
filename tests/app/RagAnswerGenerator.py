from langchain_huggingface import HuggingFaceEmbeddings  # For generating embeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter  # For splitting text into smaller chunks
from langchain_community.vectorstores import FAISS  # For storing and searching embeddings
from langchain.chains import RetrievalQAWithSourcesChain  # For retrieval-augmented question answering
from langchain_groq import ChatGroq  # Groq-based LLM integration
from langchain.schema import Document  # Schema for representing documents
import os  # For filesystem interactions

class RagAnswerGenerator:
    def __init__(self, directory):
        """
        Initializes the RAG Answer Generator with embeddings, vector store, and QA chain.
        
        Args:
            directory (str): Directory containing text files to index.
        """
        os.environ["GROQ_API_KEY"] = "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"
        self.embeddings = HuggingFaceEmbeddings(
            model_name='sentence-transformers/all-mpnet-base-v2',
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
        self.vector_store = self._create_vector_store(directory)
        self.llm = ChatGroq(
            model_name="mixtral-8x7b-32768",
            temperature=0.1,
            max_tokens=1024
        )
        self.qa_chain = RetrievalQAWithSourcesChain.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever(search_kwargs={"k": 1, "fetch_k": 8}),
            return_source_documents=True
        )

    def _create_vector_store(self, directory):
        """
        Creates a FAISS vector store from text files in the given directory.

        Args:
            directory (str): Directory containing text files.

        Returns:
            FAISS: A vector store of embeddings for the documents.
        """
        documents = [
            Document(page_content=open(os.path.join(directory, file), 'r', encoding='utf-8').read(),
                     metadata={"source": file})
            for file in os.listdir(directory) if file.endswith('.txt')
        ]
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
        chunks = text_splitter.split_documents(documents)
        return FAISS.from_documents(chunks, self.embeddings)

    def generate_answer(self, question):
        """
        Generates an answer to the given question using the QA chain.

        Args:
            question (str): User's question.

        Returns:
            str: Generated answer.
        """
        result = self.qa_chain({"question": question})
        return result.get('answer', 'Apologies, I couldn\'t find an exact answer.')
