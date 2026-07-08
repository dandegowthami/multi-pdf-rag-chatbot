# 📄 Multi-PDF RAG Chatbot

An AI-powered **Multi-PDF Question Answering System** built using **Retrieval-Augmented Generation (RAG)**. This application allows users to upload multiple PDF documents and ask natural language questions. The chatbot retrieves the most relevant document content using semantic search and generates accurate, context-aware answers using the **Groq Llama 3** model.

---

## 🚀 Features

- 📂 Upload multiple PDF documents
- 📑 Extract text from PDF files
- ✂️ Intelligent text chunking
- 🧠 Generate semantic embeddings using Sentence Transformers
- 🗄️ Store embeddings in ChromaDB vector database
- 🔍 Semantic similarity search
- 🤖 AI-generated answers using Groq Llama 3
- 📚 Displays source PDF for retrieved answers
- 🗑️ Delete uploaded documents
- 🔄 Start a new chat by clearing uploaded documents and chat history
- 💻 Clean and responsive React frontend

---

# Project Architecture

```
                +----------------+
                | Upload PDF(s)  |
                +--------+-------+
                         |
                         v
                +----------------+
                | Extract Text   |
                | (PyPDF2)       |
                +--------+-------+
                         |
                         v
                +----------------+
                | Text Chunking  |
                +--------+-------+
                         |
                         v
          +-----------------------------+
          | Sentence Transformers       |
          | all-MiniLM-L6-v2            |
          +-------------+---------------+
                        |
                        v
                +----------------+
                | ChromaDB        |
                | Vector Database |
                +--------+-------+
                         |
                         |
             User Question
                         |
                         v
            Generate Query Embedding
                         |
                         v
            Semantic Similarity Search
                         |
                         v
          Retrieve Top Relevant Chunks
                         |
                         v
             Prompt Construction
                         |
                         v
               Groq Llama 3 Model
                         |
                         v
              Context-aware Answer
```

---

# Tech Stack

## Frontend

- React.js
- CSS
- Axios

## Backend

- Python
- FastAPI
- Uvicorn

## AI & Machine Learning

- Sentence Transformers
- Groq API
- Llama 3

## Vector Database

- ChromaDB

## PDF Processing

- PyPDF2

---

# Folder Structure

```
Multi-PDF-RAG-Chatbot
│
├── Backend
│   ├── app
│   │   ├── api
│   │   ├── core
│   │   ├── models
│   │   └── services
│   │
│   ├── data
│   ├── vectorstore
│   ├── main.py
│   └── requirements.txt
│
├── Frontend
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   ├── services
│   │   └── assets
│   ├── package.json
│   └── vite.config.js
│
├── README.md
└── .gitignore
```

---

# RAG Pipeline

## Step 1: Upload PDF

Users upload one or more PDF files through the React frontend.

↓

## Step 2: Text Extraction

The backend extracts text from every page using **PyPDF2**.

↓

## Step 3: Text Chunking

Large documents are divided into smaller chunks for efficient retrieval.

↓

## Step 4: Embedding Generation

Each chunk is converted into a dense vector using

```
all-MiniLM-L6-v2
```

from Sentence Transformers.

↓

## Step 5: Store Embeddings

Embeddings are stored inside **ChromaDB** along with metadata.

↓

## Step 6: Ask Question

The user submits a natural language question.

↓

## Step 7: Query Embedding

The same embedding model converts the question into a vector.

↓

## Step 8: Semantic Search

ChromaDB retrieves the most relevant chunks based on vector similarity.

↓

## Step 9: Prompt Construction

Relevant chunks are combined with the user's question.

↓

## Step 10: LLM Response

Groq Llama 3 generates a context-aware answer using the retrieved information.

---

# Backend APIs

## Upload PDF

```
POST /upload
```

Uploads and processes PDF files.

---

## Ask Question

```
POST /ask
```

Returns answers generated using the RAG pipeline.

---

## Get Uploaded Documents

```
GET /documents
```

Returns all uploaded PDF names.

---

## Delete PDF

```
DELETE /documents/{pdf_name}
```

Deletes a selected PDF and its embeddings.

---

## Clear Chat

```
DELETE /clear
```

Clears uploaded PDFs, embeddings, and chat history.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/dandegowthami/multi-pdf-rag-chatbot.git

cd multi-pdf-rag-chatbot
```

---

## Backend

```bash
cd Backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

---

## Frontend

```bash
cd Frontend

npm install

npm run dev
```

---

# Environment Variables

Create a `.env` file inside the Backend folder.

```
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# Technologies Used

| Category | Technology |
|----------|------------|
| Programming | Python, JavaScript |
| Frontend | React.js |
| Backend | FastAPI |
| PDF Processing | PyPDF2 |
| Embedding Model | Sentence Transformers |
| Vector Database | ChromaDB |
| LLM | Groq Llama 3 |
| API Testing | Postman |
| Version Control | Git, GitHub |

---

# Future Enhancements

- User authentication
- Chat history persistence
- Support for DOCX and TXT files
- PDF summarization
- Citation highlighting
- Dark mode
- Streaming AI responses
- Cloud deployment
- Voice-based querying
- OCR support for scanned PDFs

---

# Author

**Gowthami Dande**

GitHub:
https://github.com/dandegowthami


---

# License

This project is developed for learning and educational purposes.
