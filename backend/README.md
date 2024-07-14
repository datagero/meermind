# Meermind Backend 🚀

## Introduction
Welcome to the Meermind Backend Documentation. This document provides an overview of the backend architecture, setup instructions, and a detailed description of the various components and functionalities of the Meermind application.

## Table of Contents
1. [Project Structure](#project-structure) 🗂️
2. [Setup Instructions](#setup-instructions) ⚙️
3. [API Endpoints](#api-endpoints) 🌐
4. [Database Usage and Benefits](#database-usage-and-benefits) 📊
5. [AI Tools and Benefits](#ai-tools-and-benefits) 🧠

## Project Structure 🗂️ {#project-structure}

```
backend/
├── api/
│   ├── __init__.py
│   ├── main.py
│   ├── database/
│   │   ├── create_schemas.py
│   │   ├── functions.py
│   │   ├── schemas/
│   │   │   ├── document_hash_id_schema.json
│   │   │   ├── transcript_schema.json
│   │   │   └── transcript_summary_schema.json
│   └── ai_tools/
│       ├── generate_data/
│           ├── chatagent.py
│           ├── main.py
│           ├── prompts/
│               ├── json_summaries.txt
├── requirements.txt
├── current_requirements.txt
├── pyproject.toml
├── README.md
├── .gitignore
```

### api/
- **Purpose:** Contains the main application logic and API endpoints for the Meermind project.
- **Key Components:**
  - `main.py`: The entry point for the Flask application. It defines the API endpoints and routes.
  - `database/`: Handles database interactions, schema definitions, and data management.
  - `ai_tools/`: Contains tools and scripts for AI-related functionalities such as data generation, summarization, and embeddings.

### main.py
- **Purpose:** This is the main file for running the Flask application. It initializes the app, sets up routes, and connects to the database.
- **Function:** Serves as the central hub where different components of the backend come together to handle requests and responses.

### database/
- **Purpose:** Manages all database-related operations including schema creation, data storage, and retrieval.
- **Key Components:**
  - `create_schemas.py`: Script for setting up database schemas.
  - `functions.py`: Contains functions for interacting with the database.
  - `schemas/`: Directory holding JSON schema definitions for various data types used in the project.

### ai_tools/
- **Purpose:** Contains scripts and tools for integrating AI functionalities into the application.
- **Key Components:**
  - `generate_data/`: Scripts for generating data using AI models.
  - `gptgent.py`: Contains the ChatAgent and EmbeddingAgent class responsible for generating summaries and embeddings.
  - `main.py`: Main script to initiate AI-based data processing.
  - `prompts/`: Contains prompt templates used for generating AI responses.

## Setup Instructions ⚙️ {#setup-instructions}

### Development

1. **Create a Virtual Environment:**
   ```sh
   python3 -m venv .venv
   ```

2. **Activate the Environment:**
   ```sh
   source .venv/bin/activate
   ```

3. **Install Requirements:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```sh
   flask --app api/main.py run
   ```

### Production

1. **Environment Variables:**
   Ensure you have an `.env` file in the project root folder with the following content:
   ```sh
   OPENAI_KEY_PROMPTS={Your OpenAI API Key}
   MONGODB_URI={Your MongoDB connection string}
   ```

## API Endpoints 🌐 {#api-endpoints}

### Overview
The API endpoints defined in `main.py` handle various requests related to the Meermind application's functionalities. These endpoints allow users to upload documents, generate flashcards, and manage data.

### Endpoints Summary

| Endpoint | Method | Description | Current State | Roadmap for Enhancements |
| --- | --- | --- | --- | --- |
| `/` | GET | Health check endpoint to verify if the backend is running. | Returns "Hello, World!" | None |
| `/upload` | POST, GET | Upload documents for processing. | Validates and processes .txt files, stores data in MongoDB. | Expand the file types that we can accept (video, pdf, etc.) |
| `/search_content` | POST, GET | Search for content within stored transcripts based on a search term. | Processes search term and returns top results according to threshold. | Improve search accuracy and efficiency; add advanced filtering. |
| `/get-notes` | GET | Retrieve all summaries stored in the database. | Returns a JSON array of summaries. | Add pagination, filtering, and indexing. |
| `/get-transcript/<hash>` | GET | Retrieve a specific transcript based on its hash ID. | Returns the transcript for the given hash ID. | Implement access control and add metadata. |
| `/get-note/<hash>/update` | POST | Update a specific summary based on its hash ID. | Updates document in MongoDB with new data. | Add partial updates, validation, and detailed logging. |
| `/get-note/<hash>/delete` | POST | Delete a specific summary based on its hash ID. | Deletes document from MongoDB. | Implement soft deletes and enhance security. |
| `/get-note/<hash>` | GET | Retrieve a specific summary based on its hash ID. | Returns the summary for the given hash ID. | Add more detailed response data and improve performance. |

## Database Usage and Benefits 📊 {#database-usage-and-benefits}

### MongoDB

- **Purpose:** MongoDB is used as the primary database for storing documents and vector data.
- **Benefits:**
  - **Document Store:** MongoDB's flexible schema allows for efficient storage and retrieval of various document types such as PDFs and transcripts.
  - **Vector Store:** Utilized for storing embeddings generated by AI tools, enabling efficient similarity searches and data retrieval based on content relevance.

## AI Tools and Benefits 🧠 {#ai-tools-and-benefits}

### Summarizing and Embeddings

- **Purpose:** AI tools are integrated to enhance data processing capabilities, particularly in summarizing content and generating embeddings.
- **Key Components:**
  - **Summarizing:** AI models generate concise summaries of documents, making it easier for users to extract key information.
  - **Embeddings:** AI models create vector representations of text data, which are stored in the MongoDB vector store. These embeddings allow for advanced similarity searches, improving the relevance and accuracy of information retrieval.

### Deep Dive into Embeddings

- **Embeddings Explained:**
  - Embeddings are numerical representations of text data, capturing semantic meaning and relationships between words and phrases.
  - Generated using AI models, these embeddings are stored in the database and used to compare and retrieve similar documents based on content.
  - **Benefits:** 
    - Enhanced search capabilities: Users can find relevant information quickly and accurately.
    - Improved data organization: Embeddings help in clustering and categorizing documents based on their content.

