"""
this is streamlit part
"""
# app.py - Streamlit interface for the Taiwan Legal Assistant chatbot

import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Taiwan Legal Assistant",
    page_icon="⚖️",
    layout="wide"
)

# Initialize session state to store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Taiwan Legal Assistant")
st.success("System ready!")

# Display header
st.header("Taiwan Legal Assistant")
st.markdown("Ask any questions about Taiwan's legal system in Chinese or English.")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant" and "sources" in message:
            with st.expander("View Sources"):
                for i, source in enumerate(message["sources"]):
                    st.markdown(f"**Source {i+1}:** {source}")

# Get user input
user_question = st.chat_input("Ask a legal question...")

# When user submits a question
if user_question:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_question})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_question)
    
    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        with st.spinner("Thinking..."):
            answer = "this is a test answer" 
            sources = ["test-source1", "test-source2"]
            
            # Display answer
            message_placeholder.markdown(answer)
            
            # Display sources in an expander
            with st.expander("View Sources"):
                for i, source in enumerate(sources):
                    st.markdown(f"**Source {i+1}:** {source}")
    
    # Add assistant response to chat history
    st.session_state.messages.append({
        "role": "assistant", 
        "content": answer,
        "sources": sources
    })
