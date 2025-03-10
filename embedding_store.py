# embedding_store.py - This file converts text into numbers (embeddings) that AI can understand

# Import necessary tools:
# - HuggingFaceEmbeddings: converts text to number vectors
# - Chroma: database to store these vectors
# - os and shutil: help manage files and folders
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os
import shutil

def create_vector_store(chunks, persist_directory="./chroma_db"):
    """
    This function takes text chunks and converts them to number vectors (embeddings).
    Think of it like creating a special index for a book that helps find information quickly.
    """
    # Check if we already have a vector store and remove it if it exists
    if os.path.exists(persist_directory):
        print(f"Detected existing vector store, deleting {persist_directory} directory...")
        shutil.rmtree(persist_directory)
        print("Old vector store deleted")
    
    # Initialize the embedding model (converts text to numbers)
    # We're using a model specifically trained for Chinese language
    embedding_model = HuggingFaceEmbeddings(
        model_name="shibing624/text2vec-base-chinese-paraphrase"
    )
    
    print("Creating vector store...")
    
    # Create a database to store our text chunks as vectors
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory
    )
    
    # Save the database to disk so we can use it later
    vector_store.persist()
    print(f"Vector store created and saved to {persist_directory}")
    
    return vector_store

def load_vector_store(persist_directory="./chroma_db"):
    """
    This function loads a previously created vector store from disk.
    Like reopening our special book index without having to rebuild it.
    """
    # Check if the vector store exists
    if not os.path.exists(persist_directory):
        raise ValueError(f"Vector store directory {persist_directory} does not exist")
    
    # Initialize the same embedding model we used to create the store
    embedding_model = HuggingFaceEmbeddings(
        model_name="shibing624/text2vec-base-chinese-paraphrase"
    )
    
    # Load the vector store from disk
    vector_store = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_model
    )
    
    print(f"Loaded vector store from {persist_directory}")
    return vector_store

if __name__ == "__main__":
    # This code runs when you execute this file directly
    # It tests the vector store creation
    from document_loader import process_documents
    
    # Process documents to get chunks
    chunks = process_documents()
    
    # Create a vector store from those chunks
    vector_store = create_vector_store(chunks)
    
    # Test a simple query to see if it works
    results = vector_store.similarity_search("What is the punishment for theft?", k=2)
    
    print("\nTest query results:")
    for doc in results:
        print(f"\nSource: {doc.metadata['source']}")
        print(f"Content: {doc.page_content[:150]}...")