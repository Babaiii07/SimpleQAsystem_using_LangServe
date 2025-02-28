# FastAPI LLM API

This is a FastAPI-based API that integrates with the Groq-powered Llama 3.3 70B model to provide responses based on user queries. The API is built using LangChain and LangServe.

## Features
- Uses FastAPI for serving the API.
- Integrates with Groq's `llama-3.3-70b-versatile` model.
- Utilizes LangChain for prompt templating and output parsing.
- Routes managed via LangServe for seamless integration.
- Environment variables managed via `dotenv`.

## Requirements
Ensure you have the following installed:

- Python 3.8+
- FastAPI
- Uvicorn
- LangChain
- LangServe
- LangChain Groq
- Python-dotenv

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Babaiii07/SimpleQAsystem_using_LangServe.git
   cd SimpleQAsystem_using_LangServe
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory and add:
     ```env
     GROQ_API_KEY=your_groq_api_key_here
     ```

## Usage

1. Run the FastAPI server:
   ```bash
   python langserve_Server.py
   ```

2. Access the API at:
   ```
   http://localhost:8000/qa
   ```

3. API will process queries in the following format:
   ```json
   {
     "question": "What is the capital of France?"
   }
   ```

4. The response will be:
   ```json
   {
     "answer": "Paris"
   }
   ```

## API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/qa`   | Accepts a JSON request with a `question` field and returns a response. |

## License
This project is licensed under the MIT License.

## Acknowledgments
- [FastAPI](https://fastapi.tiangolo.com/)
- [LangChain](https://python.langchain.com/)
- [Groq API](https://groq.com/)

