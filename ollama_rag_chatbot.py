"""
this is LLM part
"""

# ollama_rag_chatbot.py - This file creates the AI chatbot that answers questions using documents

# Import necessary tools:
# - os: helps interact with files and folders
# - Ollama: connects to the AI language model
# - RetrievalQA: helps create a question-answering system
# - PromptTemplate: helps format instructions for the AI
# - load_dotenv: loads environment variables
import os
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Import our custom functions from the other files
from document_loader import process_documents
from embedding_store import create_vector_store, load_vector_store

# Load environment variables from .env file
load_dotenv()

def setup_rag_system(rebuild_vector_store=False):
    """
    This function sets up the entire RAG (Retrieval-Augmented Generation) system.
    Think of it like preparing a smart assistant who can look up information in books.
    """
    # Check if we need to build or rebuild the vector store
    if rebuild_vector_store or not os.path.exists("./chroma_db"):
        print("Building vector store...")
        # Process documents to get chunks
        chunks = process_documents()
        # Create a vector store from those chunks
        vector_store = create_vector_store(chunks)
    else:
        print("Loading existing vector store...")
        # Load the existing vector store
        vector_store = load_vector_store()
    
    # Create a retriever that can find relevant information
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 2}  # Retrieve the 2 most relevant chunks
    )
    
    # Create a template for how the AI should respond
    template = """
    你是一個專業的台灣法律助手。使用以下上下文來回答最後的問題。
    如果你不知道答案，就直說不知道，不要試圖編造答案。
    請用繁體中文（台灣用語）回答問題，避免使用簡體中文詞彙。
    
    Context:
    {context}
    
    Question: {question}
    
    Answer:
    """
    
    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )
    
    # Initialize the language model (the AI brain)
    llm = Ollama(
        model="qwen:7b",  # Using a Chinese-capable model
        temperature=0.2  # Lower temperature for more factual responses
    )
    
    # Create the RAG chain that connects everything
    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  # "stuff" means we put all retrieved documents into the prompt
        retriever=retriever,
        return_source_documents=True,  # Return source documents for reference
        chain_type_kwargs={"prompt": prompt}
    )
    
    return rag_chain

def ask_question(rag_chain, question):
    """
    This function sends a question to the RAG system and gets an answer.
    Like asking a librarian a question who then looks up information.
    """
    # Get response from the RAG chain
    response = rag_chain.invoke({"query": question})
    
    # Extract the answer and source documents
    answer = response["result"]
    source_docs = response["source_documents"]
    
    return answer, source_docs

def main():
    """
    This is the main function that runs the chatbot.
    It sets up the system and handles the conversation loop.
    """
    print("Setting up RAG system...")
    rag_chain = setup_rag_system()
    
    print("\nTaiwan Legal Assistant is ready! Type 'exit' to quit.")
    
    while True:
        # Get the user's question
        question = input("\nYour question: ")
        
        # Exit if the user types 'exit'
        if question.lower() == 'exit':
            break
        
        # Get the answer
        answer, source_docs = ask_question(rag_chain, question)
        
        # Print the answer
        print("\nAnswer:")
        print(answer)
        
        # Print the sources
        print("\nSources:")
        for i, doc in enumerate(source_docs):
            print(f"Source {i+1}: {doc.metadata['source']}")

if __name__ == "__main__":
    main()