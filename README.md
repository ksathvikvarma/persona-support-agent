# Persona-Based AI Support Agent

An AI-powered customer support assistant that combines Persona Classification, Retrieval-Augmented Generation (RAG), and Escalation Workflows to deliver context-aware and persona-specific responses.

---

## Overview

This project simulates an intelligent customer support system capable of:

* Detecting customer personas from user messages
* Retrieving relevant information from a knowledge base using semantic search
* Generating persona-aware responses using Gemini
* Escalating sensitive or unsupported requests
* Creating structured handoff summaries for human agents
* Providing an interactive web interface using Streamlit
* Displaying classification confidence scores and reasoning
* Handling transient AI API failures through retry mechanisms

---

## Current Capabilities

* Persona Classification with confidence scoring
* Retrieval-Augmented Generation (RAG)
* Semantic search using vector embeddings
* Persona-aware response generation
* Human escalation workflow
* Structured handoff summaries
* Streamlit web application
* Retry handling for Gemini API rate limits and temporary failures
* Cloud deployment using Streamlit Community Cloud

---

## Features

### Persona Classification

Identifies one of the following customer personas:

* Technical Expert
* Frustrated User
* Business Executive

The classifier returns:

* Detected persona
* Confidence score
* Classification reasoning

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

### Confidence Scoring

The persona classifier provides:

* Predicted persona
* Confidence score
* Classification reasoning

This improves transparency and helps evaluate classification quality.

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

### Reliability Features

The system includes automatic retry handling for:

* Gemini API rate limits (429)
* Temporary service unavailability (503)

This improves application stability during transient API failures.

### Interactive Streamlit UI

* Web-based interface
* Persona visibility
* Confidence score visibility
* Classification reasoning visibility
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
(Confidence + Reasoning)
    │
    ▼
Embedding Generation
    │
    ▼
Vector Retrieval (ChromaDB)
    │
    ▼
Escalation Check
    │
    ├── Escalation Required
    │         │
    │         ▼
    │   Handoff Summary
    │
    └── No Escalation
              │
              ▼
      Persona-Aware Response
```

---

## AI Engineering Concepts Demonstrated

This project demonstrates practical implementation of:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search
* Embedding Models
* Prompt Engineering
* Persona Classification
* Human-in-the-Loop Escalation
* Confidence Scoring
* Retry and Resilience Patterns
* Streamlit Deployment

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

## Deployment

The application is deployed using Streamlit Community Cloud.

Deployment includes:

* Automated GitHub integration
* Secure secret management
* Cloud-hosted Streamlit interface

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

### Escalation Example

```text
I want my account permanently deleted.
```

### Legal Escalation Example

```text
I would like to discuss legal action regarding this issue.
```

---

## Resume Highlights

* Built an AI-powered customer support assistant using Gemini, ChromaDB, and Streamlit.
* Implemented Retrieval-Augmented Generation (RAG) with semantic document retrieval.
* Developed persona classification with confidence scoring and reasoning.
* Designed adaptive response generation for Technical Expert, Frustrated User, and Business Executive personas.
* Implemented escalation workflows and structured human handoff summaries.
* Added retry handling for Gemini API rate limits and transient failures.
* Deployed a production-ready web application using Streamlit Community Cloud.

---

## Project Evolution

### v1.0

* Persona Detection
* RAG Pipeline
* Escalation Workflow
* Human Handoff Summary
* Streamlit Interface

### v1.1

* Confidence Scores
* Classification Reasoning
* Gemini Retry Handling
* Streamlit Cloud Deployment

### Planned v1.2

* Multi-turn Conversation Memory
* Retrieval Confidence Thresholds
* Chat-style Streamlit Interface

---

## Planned Enhancements

### High Priority

* Multi-turn conversation memory
* Retrieval confidence-based escalation
* Chat-style Streamlit interface

### Medium Priority

* User feedback collection
* Analytics dashboard
* Persistent conversation storage using SQLite

### Advanced

* LangGraph workflow orchestration
* Multi-agent architecture
* Automated evaluation framework
* Retrieval performance metrics

---

## Author

**K. Sathvik Varma**
