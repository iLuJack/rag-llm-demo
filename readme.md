# RAG & LLM Demo

This project demonstrates a Retrieval-Augmented Generation (RAG) chatbot using Ollama and LangChain. The chatbot can answer questions about legal documents in Traditional Chinese, specifically the Civil Law text included in the data directory.

## Project Structure

- `document_loader.py` - Loads and processes text documents
- `embedding_store.py` - Creates and manages vector embeddings for document chunks
- `ollama_rag_chatbot.py` - Main chatbot implementation using Ollama and RAG
- `data/` - Directory containing demo text documents (民法、刑法、公司法原文)
- `.env` - Environment file for API keys or tokens (not included in repo)

## Generated Files and Outputs

When you run the code, it will create several files and directories:

- `chroma_db/` - Directory created by `embedding_store.py` that contains:
  - Vector embeddings of your document chunks
  - Metadata about your documents
  - Index files for fast retrieval
  
  This database allows the system to quickly find relevant information when you ask questions.

- `venv/` - Directory created during setup that contains the Python virtual environment

- Terminal outputs:
  - `document_loader.py` will show which documents were loaded and how many chunks were created
  - `embedding_store.py` will show the creation of the vector store and test query results
  - `ollama_rag_chatbot.py` will show the chatbot interface where you can ask questions

The workflow is:
1. `document_loader.py` reads text files from `data/` and splits them into chunks
2. `embedding_store.py` converts these chunks into vectors and stores them in `chroma_db/`
3. `ollama_rag_chatbot.py` uses the `chroma_db/` to find relevant information when answering questions

## Requirements

- Python 3.9.13
- Dependencies listed in `requirements.txt`

## Setup for Non-Coders

### Step 1: Install Python (Windows)

1. Download Python 3.9.13 installer from the official website:
   - Go to: https://www.python.org/downloads/release/python-3913/
   - Scroll down and click on "Windows installer (64-bit)" to download

2. Run the installer:
   - Check the box that says "Add Python 3.9 to PATH"
   - Click "Install Now"
   - Wait for installation to complete
   - Click "Close" when finished

3. Verify installation:
   - Open Command Prompt (search for "cmd" in the Start menu)
   - Type `python --version` and press Enter
   - You should see "Python 3.9.13"

### Step 1: Install Python (Mac)

1. Install Homebrew (if not already installed):
   - Open Terminal
   - Paste this command and press Enter:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

2. Install Python 3.9.13:
   - In Terminal, run:
     ```bash
     brew install python@3.9
     ```

3. Verify installation:
   - In Terminal, run:
     ```bash
     python3.9 --version
     ```
   - You should see "Python 3.9.13"

### Step 2: Download This Project

You have two options to download the project:

#### Option 1: Download ZIP (No Git required)

1. Download this project as a ZIP file:
   - Click the green "Code" button at the top of the GitHub page
   - Select "Download ZIP"
   - Save the ZIP file to your computer

2. Extract the ZIP file:
   - Right-click the ZIP file and select "Extract All..." (Windows) or double-click (Mac)
   - Choose a location where you want to extract the files
   - Click "Extract"

#### Option 2: Clone with Git (For users familiar with Git)

1. Install Git if you don't have it:
   - Windows: Download and install from https://git-scm.com/download/win
   - Mac: Run `brew install git` in Terminal

2. Open Command Prompt (Windows) or Terminal (Mac)

3. Navigate to the directory where you want to store the project

4. Clone the repository:
   ```bash
   git clone https://github.com/iLuJack/rag-llm-demo.git
   ```

5. Navigate into the project directory:
   ```bash
   cd rag-llm-demo
   ```

### Step 3: Set Up the Project (Windows)

1. Open Command Prompt:
   - Press Win+R, type "cmd", and press Enter
   - Navigate to the project folder:
     ```
     cd path\to\extracted\folder
     ```
     (Replace "path\to\extracted\folder" with the actual path where you extracted the files)

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   ```
   venv\Scripts\activate
   ```
   (You should see "(venv)" at the beginning of the command line)

4. Install required packages:
   ```
   pip install -r requirements.txt
   ```
   (This might take a few minutes)

### Step 3: Set Up the Project (Mac)

1. Open Terminal:
   - Press Cmd+Space, type "Terminal", and press Enter
   - Navigate to the project folder:
     ```
     cd path/to/extracted/folder
     ```
     (Replace "path/to/extracted/folder" with the actual path where you extracted the files)

2. Create a virtual environment:
   ```
   python3.9 -m venv venv
   ```

3. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```
   (You should see "(venv)" at the beginning of the command line)

4. Install required packages:
   ```
   pip install -r requirements.txt
   ```
   (This might take a few minutes)

### Step 4: Install Ollama

1. Download Ollama:
   - Go to https://ollama.ai/download
   - Download the appropriate version for your operating system (Windows or Mac)

2. Install Ollama:
   - Windows: Run the downloaded installer and follow the prompts
   - Mac: Drag the Ollama app to your Applications folder

3. Start Ollama:
   - Windows: Ollama should start automatically after installation
   - Mac: Open the Ollama app from your Applications folder

4. Pull a model:
   - Windows: Open Command Prompt and run:
     ```
     ollama pull qwen:7b
     ```
   - Mac: Open Terminal and run:
     ```
     ollama pull qwen:7b
     ```
   (This will download the model, which might take some time depending on your internet speed)

### Step 5: Run the Chatbot

1. Make sure your virtual environment is activated (you should see "(venv)" at the beginning of the command line)

2. Process the documents (only needed once):
   - Windows:
     ```
     python document_loader.py
     python embedding_store.py
     ```
   - Mac:
     ```
     python document_loader.py
     python embedding_store.py
     ```

3. Start the chatbot:
   - Windows:
     ```
     python ollama_rag_chatbot.py
     ```
   - Mac:
     ```
     python ollama_rag_chatbot.py
     ```

4. Ask questions:
   - Type your question about Taiwan Civil Law in the terminal
   - The chatbot will respond with an answer based on the documents
   - Type "exit" to quit the chatbot

## Troubleshooting

### Common Issues:

1. **"Python is not recognized as an internal or external command"**:
   - Make sure Python is installed correctly
   - Try restarting your computer
   - Check if Python is added to PATH during installation

2. **"No module named 'langchain'"**:
   - Make sure you've activated the virtual environment
   - Try reinstalling the requirements:
     ```
     pip install -r requirements.txt
     ```

3. **Ollama connection errors**:
   - Make sure Ollama is running
   - Check if the model was downloaded correctly
   - Try restarting Ollama

4. **Out of memory errors**:
   - The AI model requires significant RAM
   - Close other applications to free up memory
   - Try using a smaller model (change "qwen:7b" to a smaller model in the code)

## How It Works (For the Curious)

1. **Document Processing**: The system reads text files and breaks them into smaller pieces.

2. **Creating Embeddings**: It converts these text pieces into number patterns (vectors) that represent the meaning of the text.

3. **Storing Information**: These vectors are stored in a special database that can quickly find related information.

4. **Answering Questions**: When you ask a question:
   - The system converts your question into a vector
   - It finds the most relevant text pieces in the database
   - It sends your question and the relevant text to the AI model
   - The AI generates an answer based on the provided information

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.