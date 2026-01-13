# LangGraph Beginner Project

A simple LangGraph agent powered by Groq's Llama 3 models suitable for beginners. This project demonstrates a basic agent loop with a generation and verification step.

## Features

- **LangGraph**: Orchestrates the agent workflow.
- **Groq API**: Uses `llama-3.3-70b-versatile` for fast inference.
- **Streamlit UI**: Provides an interactive chat interface.
- **Verification Loop**: Automatically checks answer quality and retries if necessary.

## Setup

1.  **Clone the repository** (if applicable).
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Environment Variables**:
    Create a `.env` file in the root directory and add your Groq API key:
    ```env
    GROQ_API_KEY=your_api_key_here
    ```

## Usage

### Run the backend only
```bash
python app.py
```

### Run the Streamlit UI
```bash
streamlit run ui.py
```
