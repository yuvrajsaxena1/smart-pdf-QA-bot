<p align="center">
  <img src="https://img.shields.io/badge/Project-Smart%20PDF%20Q%26A%20Bot-blue.svg?style=for-the-badge" alt="Project Badge">
</p>

<h1 align="center">🧠 Smart PDF Q&A Bot 🤖</h1>
<p align="center">Your Intelligent Assistant for PDF Documents</p>

<p align="center">
  <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3.7+-blue.svg?style=flat-square" alt="Python Version">
  </a>
  <a href="https://github.com/hwchase17/langchain">
    <img src="https://img.shields.io/badge/LangChain-Latest-orange.svg?style=flat-square" alt="LangChain">
  </a>
  <a href="https://streamlit.io/">
    <img src="https://img.shields.io/badge/Streamlit-Latest-brightgreen.svg?style=flat-square" alt="Streamlit">
  </a>
</p>

<br>

👋 Welcome to the **Smart PDF Q&A Bot** project! This application empowers you to interact with your PDF documents in a whole new way. Simply upload a PDF, and you can ask natural language questions to get insightful answers directly extracted from the document's content. Leveraging the power of LangChain and Retrieval-Augmented Generation (RAG), this bot provides intelligent and context-aware responses.

## ✨ Key Features

* **📤 Easy PDF Upload:** Effortlessly upload your PDF documents through a user-friendly interface.
* **📄 Text Extraction & Chunking:** The bot intelligently extracts text content from your PDF and divides it into manageable chunks.
* **<0xF0><0x9F><0x97><0x8E>️ Vector Database Storage:** Utilizes either FAISS or ChromaDB to store the document chunks as vector embeddings for efficient semantic search.
* **🧠 Smart Question Answering:** Ask questions in plain English and receive relevant answers derived directly from the PDF content.
* **🚀 Powered by LLMs:** Integrates with powerful Large Language Models (LLMs) like GPT-3.5 or GPT-4 (via OpenAI) to understand your queries and generate accurate responses.
* **<0xF0><0x9F><0xAA><0xB6> Streamlit Interface:** Provides a clean and intuitive web interface built with Streamlit for seamless interaction.

## 🛠️ Tech Stack

This project is built using the following cutting-edge technologies:

* **🐍 Python:** The primary programming language.
* **🔗 LangChain:** A powerful framework for building applications powered by large language models.
* **<0xF0><0x9F><0xA7><0xAE> Vector Databases:**
    * **FAISS:** A library for efficient similarity search and clustering of dense vectors.
    * **ChromaDB:** An open-source embedding database.
    *(You can choose either for your project)*
* **🔑 OpenAI Embeddings:** Used to create numerical representations (embeddings) of the text chunks, capturing their semantic meaning.
* **🤖 OpenAI LLM (GPT-3.5/GPT-4):** The core language model responsible for understanding questions and generating answers based on the retrieved document context.
* **<0xF0><0x9F><0xAA><0xB6> Streamlit:** A Python library for rapidly building and sharing beautiful, custom web applications for machine learning and data science.

## ⚙️ Setup and Installation

Follow these steps to get the Smart PDF Q&A Bot up and running on your local machine:

1.  **Clone the Repository:**
    ```bash
    git clone <YOUR_REPOSITORY_URL>
    cd smart-pdf-qa-bot
    ```

2.  **Install Dependencies:**
    It's recommended to create a virtual environment to manage the project dependencies.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # venv\Scripts\activate   # On Windows
    pip install -r requirements.txt
    ```

3.  **Set up OpenAI API Key:**
    You'll need an OpenAI API key to use their embeddings and language models.
    * Sign up for an OpenAI account [here](https://openai.com/).
    * Generate an API key from your dashboard.
    * Store this API key securely, for example, as an environment variable named `OPENAI_API_KEY`.

4.  **Running the Streamlit Application:**
    Navigate to the project directory in your terminal and run:
    ```bash
    streamlit run app.py
    ```
    This command will launch the Streamlit application in your web browser.

## 🚀 How to Use

1.  **Upload PDF:** On the Streamlit interface, you'll find an "Upload PDF" section. Click on the "Browse files" button and select the PDF document you want to query.
2.  **Ask Questions:** Once the PDF is processed, a text input box will appear where you can type your natural language questions related to the content of the uploaded PDF.
3.  **Get Answers:** Hit Enter or click the "Ask" button. The bot will process your question, search the relevant information within the PDF, and provide you with a concise and informative answer.

## 📂 Project Structure
smart-pdf-qa-bot/
├── app.py             # The main Streamlit application script
├── utils.py           # Utility functions for PDF processing and data handling
├── vector_store.py    # Logic for creating and interacting with the vector database
├── requirements.txt   # List of project dependencies
└── README.md          # This README file
# 🤝 Contributions

Contributions to this project are welcome! If you have ideas for improvements, bug fixes, or new features, feel free to open an issue or submit a pull request. Please follow standard GitHub practices.


## 🎉 Acknowledgements

* The amazing developers of **LangChain** for providing such a powerful and versatile framework.
* The creators of **FAISS** and **ChromaDB** for their efficient vector database solutions.
* **OpenAI** for their state-of-the-art language models and embeddings.
* The **Streamlit** team for making web application development for data science so accessible.
