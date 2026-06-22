# Persona-Based AI Support Agent

An AI-powered customer support assistant that combines Persona Classification, Retrieval-Augmented Generation (RAG), and Escalation Workflows to deliver context-aware and persona-specific responses.

## Overview

This project simulates an intelligent customer support system capable of:

* Detecting customer personas from user messages
* Retrieving relevant information from a knowledge base using semantic search
* Generating persona-aware responses using Gemini
* Escalating sensitive or unsupported requests
* Creating structured handoff summaries for human agents
* Providing an interactive web interface using Streamlit

---

## Features

### Persona Detection

Identifies one of the following customer personas:

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

Responses are tailored based on the detected persona:

* Technical Expert → Detailed and technical responses
* Frustrated User → Empathetic and reassuring responses
* Business Executive → Concise and business-focused responses

### Escalation Workflow

Automatically escalates:

* Account deletion requests
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

### Interactive Streamlit UI

* Simple web interface
* Persona visibility
* Source visibility
* Escalation display
* Handoff summary visualization

---

## System Architecture

```text
User Query
    │
    ▼
Persona Classification
    │
    ▼
Knowledge Retrieval (RAG)
    │
    ▼
Response Generation
    │
    ▼
Escalation Check
    │
    ├── No Escalation → AI Response
    │
    └── Escalation Required
            │
            ▼
      Handoff Summary
```

---

## Tech Stack

### AI & LLM

* Google Gemini 2.5 Flash
* Gemini Embeddings

### Retrieval

* ChromaDB
* LangChain Text Splitters

### Backend

* Python

### Interface

* Streamlit

### Document Processing

* PyPDF

### Configuration

* Python Dotenv

---

## Project Structure

```text
persona-support-agent/
│
├── app.py
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── data/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── classifier.py
│   ├── generator.py
│   ├── rag_pipeline.py
│   ├── escalator.py
│   └── handoff.py
│
└── chroma_db/
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

You can also use:

```env
.env.example
```

as a template.

---

## Running the Application

### Build the Vector Database

Run once after adding documents:

```bash
python src/rag_pipeline.py
```

### Run CLI Version

```bash
python app.py
```

### Run Streamlit UI

```bash
streamlit run streamlit_app.py
```

---

## Example Queries

### Technical Expert

```text
My API requests are returning a 401 authentication error.
```

### Frustrated User

```text
I have been locked out of my account for days and nothing is working.
```

### Business Executive

```text
This outage is affecting our operations. What is the expected resolution timeline?
```

### Escalation

```text
I want my account permanently deleted.
```

---

## Resume Highlights

* Built a Retrieval-Augmented Generation (RAG) customer support system using Gemini and ChromaDB.
* Implemented persona classification and adaptive response generation.
* Designed a semantic retrieval pipeline using vector embeddings and similarity search.
* Developed an escalation workflow with automated human handoff summaries.
* Created an interactive Streamlit-based user interface for AI-powered customer support.

---

## Future Enhancements

* Conversation Memory
* Retrieval Confidence Scores
* Source Citation Display
* Enhanced Escalation Policies
* Multi-turn Conversations
* Streamlit Cloud Deployment

---

## Author

K. Sathvik Varma
