# 📄 RAG-Based Document Question Answering System

A Retrieval-Augmented Generation (RAG) application that enables users to ask natural language questions from a PDF document. The system retrieves the most relevant document sections using semantic search with FAISS and HuggingFace embeddings, then generates context-aware answers using Google's Gemini model.

---

## 📌 Project Overview

Traditional Large Language Models may generate answers without relying on a specific document. This project implements the Retrieval-Augmented Generation (RAG) architecture, where answers are generated only after retrieving relevant information from a PDF.

The application consists of:

- CLI (Command Line Interface)
- Streamlit Web Application

The system first indexes the PDF into vector embeddings using HuggingFace Sentence Transformers and stores them in a FAISS vector database. Whenever a user asks a question, the application retrieves the most relevant chunks and sends them as context to the Gemini LLM.

---

# 🚀 Features

- PDF document processing
- Automatic text chunking
- Semantic search using vector embeddings
- FAISS vector database
- Google Gemini integration
- Command Line Interface
- Streamlit Web Interface
- Prompt Engineering
- Cached vector database loading
- Exception handling
- User-friendly interface

---

# 🏗️ Project Architecture

```
                    PDF Document
                          │
                          ▼
                PyPDF Document Loader
                          │
                          ▼
          Recursive Character Text Splitter
                          │
                          ▼
        HuggingFace Embedding Model
 (sentence-transformers/all-MiniLM-L6-v2)
                          │
                          ▼
               FAISS Vector Database
                          │
          ┌───────────────┴───────────────┐
          │                               │
          ▼                               ▼
      CLI Version                 Streamlit App
          │                               │
          ▼                               ▼
       User Question               User Question
          │                               │
          ▼                               ▼
      Similarity Search (FAISS)
                          │
                          ▼
               Top Relevant Chunks
                          │
                          ▼
                Prompt Engineering
                          │
                          ▼
                Google Gemini Model
                          │
                          ▼
                  Generated Answer
```

---

# 📂 Project Structure

```
Week-7_Assignment/
│
├── app.py
├── rag.py
├── create_vector_db.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── data/
│     └── Cryptographic Solutions.pdf
│
├── vector_db/
│     ├── index.faiss
│     └── index.pkl
│
└── .streamlit/
      └── config.toml
```

---

# 🛠️ Tech Stack

### Programming Language

- Python 3.11+

### Frameworks

- LangChain
- Streamlit

### LLM

- Google Gemini

### Embedding Model

- sentence-transformers/all-MiniLM-L6-v2

### Vector Database

- FAISS

### Libraries

- google-generativeai
- langchain-community
- langchain-huggingface
- sentence-transformers
- faiss-cpu
- pypdf
- python-dotenv

---

# ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory

```bash
cd Week-7_Assignment
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```
GOOGLE_API_KEY=YOUR_API_KEY
```

---

# 📄 Building the Vector Database

Generate embeddings and create the FAISS index.

```bash
python create_vector_db.py
```

This process:

- Reads the PDF
- Splits text into chunks
- Generates embeddings
- Creates FAISS index
- Saves the vector database

---

# 💻 Running the CLI Application

```bash
python rag.py
```

Example

```
Question:
What is Cryptography?

Answer:
Cryptography is a technique used to secure digital information...
```

---

# 🌐 Running the Streamlit Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

Features:

- Question input box
- Loading spinner
- Context retrieval
- AI-generated answer
- Error handling

---

# 🔄 Workflow

1. Load PDF
2. Split into text chunks
3. Generate embeddings
4. Store embeddings in FAISS
5. User asks a question
6. Convert question into embedding
7. Retrieve similar chunks
8. Build context
9. Send prompt to Gemini
10. Display answer

---

# 🧠 Prompt Engineering

The application instructs the LLM to answer only from the retrieved context.

Example Prompt:

```
You are a helpful AI assistant.

Answer only using the provided context.

If the answer is unavailable, reply:

"I couldn't find the answer in the provided document."

Context:
...

Question:
...

Answer:
```

---

# 📊 Concepts Demonstrated

- Retrieval-Augmented Generation (RAG)
- Large Language Models
- Vector Embeddings
- Semantic Search
- FAISS Indexing
- Prompt Engineering
- HuggingFace Embeddings
- Google Gemini
- Document Question Answering
- Context Retrieval
- Streamlit Deployment

---

# 📸 Sample Output

### CLI

```
Question:
What is Cryptography?

Answer:
Cryptography protects digital information by converting readable data into secure encrypted information that can only be accessed by authorized users.
```

---

### Streamlit

- User enters a question.
- System retrieves relevant document chunks.
- Gemini generates the response.
- Answer is displayed on the webpage.

---

# 🔮 Future Enhancements

- Multiple PDF support
- PDF upload through UI
- Conversation history
- Source citation display
- Hybrid search
- OCR support for scanned PDFs
- Persistent chat sessions
- Support for multiple LLM providers

---

# 👨‍💻 Author

**Rudra Abhishek**

B.Tech Computer Science & Engineering

ITER, SOA University

GitHub:
https://github.com/rudraAbhishek8763

---

# 📜 License

This project was developed as part of the **Celebal Technologies Data Science Internship – Week 7 Assignment**.

It is intended for educational and learning purposes.
