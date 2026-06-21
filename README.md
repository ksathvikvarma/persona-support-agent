# Persona-Based AI Support Agent

An AI-powered customer support assistant that combines Persona Classification, Retrieval-Augmented Generation (RAG), and Escalation Workflows to provide context-aware and persona-specific support responses.

## Overview

This project simulates an intelligent customer support system capable of:

* Detecting customer personas from incoming messages
* Retrieving relevant information from a knowledge base using semantic search
* Generating persona-aware responses using Gemini
* Escalating sensitive or unsupported issues
* Creating structured handoff summaries for human agents

The system is designed to improve customer support quality by adapting communication style based on user behavior and intent.

---

## Key Features

### Persona Classification

Detects one of the following customer personas:

* Technical Expert
* Frustrated User
* Business Executive

### Retrieval-Augmented Generation (RAG)

* Loads knowledge base documents from TXT, Markdown, and PDF files
* Splits documents into semantic chunks
* Generates embeddings using Gemini Embeddings
* Stores vectors in ChromaDB
* Retrieves the most relevant context for user queries

### Persona-Aware Response Generation

Responses are tailored according to the detected persona:

* Technical Expert → Detailed and technical explanations
* Frustrated User → Empathetic and reassuring responses
* Business Executive → Concise and business-focused communication

### Escalation Workflow

Automatically escalates:

* Sensitive account actions
* Legal concerns
* Billing disputes
* Unsupported requests
* Queries without sufficient knowledge base coverage

### Human Handoff Summary

Generates structured summaries containing:

* Detected persona
* User issue
* Conversation history
* Knowledge sources used
* Escalation reasons
* Recommended next action

---

## System Architecture

```text
User Query
    │
    ▼
Persona Classification
    │
    ▼
Knowledge Base Retrieval (RAG)
    │
    ▼
Response Generation
    │
    ▼
Escalation Check
    │
    ├── No Escalation → Return AI Response
    │
    └── Escalation Required
            │
            ▼
      Handoff Summary
```

---

## Tech Stack

* Python
* Google Gemini API (gemini-2.5-flash)
* Google Gemini Embeddings (gemini-embedding-001)
* ChromaDB
* LangChain Text Splitters
* PyPDF
* Python Dotenv

---

## Project Structure

```text
persona-support-agent/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│
├── chroma_db/
│
└── src/
    ├── __init__.py
    ├── config.py
    ├── classifier.py
    ├── generator.py
    ├── rag_pipeline.py
    ├── escalator.py
    └── handoff.py
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd persona-support-agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Running the Application

### Build the Vector Database

The first time you run the project, create the vector database:

```python
from src.rag_pipeline import load_documents, chunk_documents, create_vector_db

docs = load_documents()
chunks = chunk_documents(docs)
create_vector_db(chunks)
```

### Start the Application

```bash
python app.py
```

---

## Example Interaction

### User Query

```text
My API requests are returning a 401 authentication error.
```

### Detected Persona

```text
Technical Expert
```

### Retrieved Sources

```text
api_authentication.md
integration_guide.md
```

### Generated Response

```text
A detailed troubleshooting response based on retrieved documentation.
```

---

## Escalation Example

### User Query

```text
I want my account deleted permanently.
```

### Result

```text
ESCALATION REQUIRED

Reason:
Sensitive issue detected: delete
```

---

## Configuration

Application settings are managed through:

```text
src/config.py
```

Examples:

* Chunk size
* Chunk overlap
* Retrieval count
* Collection name
* Embedding model
* Generation model
* Escalation keywords

---

## Future Improvements

* Streamlit UI
* FastAPI backend
* REST API endpoints
* Deployment on Streamlit Cloud or Render
* Retrieval confidence scoring
* Multi-collection support
* Conversation memory
* User feedback collection

---

## Resume Highlights

* Built a Retrieval-Augmented Generation (RAG) support system using Gemini and ChromaDB.
* Implemented persona classification and adaptive response generation.
* Designed an escalation workflow with automated handoff summaries.
* Developed a modular and configurable AI support architecture.

---

## Author

Sathvik Varma
