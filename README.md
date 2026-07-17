#  YouTube RAG Chatbot

## 📌 Project Overview

The **YouTube RAG Chatbot** is a Retrieval-Augmented Generation (RAG) application that enables users to ask questions about any public YouTube video. It extracts the video's transcript and metadata, converts the transcript into vector embeddings, stores them in ChromaDB, and generates accurate, context-aware answers using Mistral AI.

---

## ❓ Problem Statement

Long YouTube videos such as lectures, podcasts, interviews, and webinars contain valuable information, but finding specific details often requires watching the entire video or manually searching through transcripts. This process is time-consuming and inefficient.

---

## 💼 Business Use Case

This application can be used by:

- 🎓 Students to quickly understand educational videos.
- 🔬 Researchers to extract information from interviews and podcasts.
- 🎥 Content creators to summarize videos and find key discussion points.
- 🏢 Organizations to build searchable knowledge bases from recorded meetings, webinars, and training sessions.

---

## ✅ Problems Solved

- Reduces the time required to search through long videos.
- Enables natural language question answering over video transcripts.
- Uses semantic search for accurate information retrieval.
- Minimizes hallucinations by grounding responses in the retrieved transcript.
- Includes video metadata (title, channel, views, etc.) to answer metadata-related questions.

---

## ✨ Key Features

- Process any public YouTube video.
- Fetch video transcripts automatically.
- Retrieve video metadata.
- Semantic search using Cohere Embeddings.
- ChromaDB vector database for efficient retrieval.
- Context-aware answers using Mistral AI.
- Interactive Streamlit user interface.

---

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Framework:** LangChain
- **Frontend:** Streamlit
- **LLM:** Mistral AI
- **Embedding Model:** Cohere Embeddings (`embed-english-v3.0`)
- **Vector Database:** ChromaDB
- **APIs:** YouTube Data API v3, YouTube Transcript API

---

## 🔄 Project Workflow

```text
YouTube URL
      │
      ▼
Fetch Transcript & Metadata
      │
      ▼
Create LangChain Document
      │
      ▼
Text Splitting
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Generate Answer using Mistral AI
```
