
# Meermind Project Overview 🚀

Welcome to Meermind, an innovative tool designed to help students and professionals manage information overload and improve collaboration. This project aims to make learning more efficient, increase productivity, and enhance the retention of important information by creating study aids from video transcripts, with a roadmap to enable PDF documents, video, and other formats.

Students struggle with disorganized and time-consuming note-taking, making it hard to collaborate and revisit information. Meermind provides a consistent, AI-powered solution to streamline note-taking, improve information retrieval, and enhance study efficiency.

🏆 Winner "Best Use of MongoDB Atlas" in the "Hack Your Portfolio" MLH Hackathon 🎉

📽️ While we work on a functional demo version, please [watch this video](https://www.youtube.com/watch?v=E7RLCFmFN2o&ab_channel=MatiasV) to get an overview of the project.

## Repository Overview 
This document provides a high-level overview of the entire project structure, including key directories and components. It serves as a guide to understanding the layout and functionality of the codebase.

Tech stak includes REACT, Flask, ChatGPT, MongoDB Atlas, and use of Embeddings & Vectors.

## Data Directory 📊
The `data/` directory contains sample data and initial datasets used for getting started with understanding the Meermind application. Normally, you would upload files through the UI and these will get persisted in your MongoDB.

## Frontend Directory 💻

### Overview
The `frontend/` directory contains the React-based user interface for the Meermind application. It manages the client-side code, providing an interactive and user-friendly experience.


Refer to `frontend/README.md` for detailed information about setting up and running the frontend.

## Backend Directory 🧩

### Overview
The `backend/` directory contains configuration files, dependencies, and scripts for setting up and running the backend application.

Refer to `backend/README.md` for detailed information about setting up and running the backend.

## Setup Instructions ⚙️

Follow the specific instructions for the backend/ and frontend/ directories. 

1. **Environment Variables:**
   Ensure you have an `.env` file in the project root folder with the following content:
   ```sh
   OPENAI_KEY_PROMPTS={Your OpenAI API Key}
   MONGODB_URI={Your MongoDB connection string}
   ```


# By: Matias V, Meghna P, Carlos T, Hemraj P
