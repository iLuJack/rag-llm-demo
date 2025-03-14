"""
this is RAG part
"""
# document_loader.py - This file handles loading and preparing text documents

# Import necessary tools:
# - TextLoader: helps read text files
# - RecursiveCharacterTextSplitter: breaks long texts into smaller chunks
# - os: helps interact with files and folders on your computer
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def load_documents(directory_path):
    """
    This function finds and loads all text files from a folder.
    Think of it like gathering all books from a bookshelf.
    """
    documents = []  # Empty list to store our documents
    
    # Look through all files in the specified folder
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):  # Only process text files
            file_path = os.path.join(directory_path, filename)
            try:
                # Load the document with proper encoding for Chinese characters
                loader = TextLoader(file_path, encoding='utf-8')
                documents.extend(loader.load())
                print(f"Loaded document: {filename}")
            except Exception as e:
                print(f"Error loading {filename}: {e}")
    
    return documents  # Return all the loaded documents

def split_documents(documents):
    """
    This function breaks long documents into smaller, manageable pieces.
    Like cutting a long book into chapters for easier reading.
    """
    # Create a text splitter optimized for Traditional Chinese
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,  # Each chunk will be about 400 characters
        chunk_overlap=80,  # Chunks overlap by 80 characters to maintain context
        length_function=len,
        # These are the characters where the text can be split (punctuation marks)
        separators=["\n\n", "\n", "。", "！", "？", "，", "；", "：", "　", " ", ""]
    )
    
    # Split the documents into chunks
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks")
    
    return chunks

def process_documents(directory_path="./data"):
    """
    This is the main function that handles the entire document processing workflow.
    It loads documents and splits them into chunks.
    """
    # Load all documents from the data folder
    documents = load_documents(directory_path)
    
    # Split those documents into smaller chunks
    chunks = split_documents(documents)
    
    return chunks

if __name__ == "__main__":
    # This code runs when you execute this file directly
    # It tests the document loading and processing
    chunks = process_documents()
    
    # Print a sample chunk to verify everything worked
    if chunks:
        print("\nSample chunk content:")
        print(f"Content: {chunks[0].page_content[:150]}...")
        print(f"Source: {chunks[0].metadata['source']}")
    else:
        print("No documents were processed.")