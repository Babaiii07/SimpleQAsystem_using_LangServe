from fastapi import FastAPI
import uvicorn
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY


model = ChatGroq(model="llama-3.3-70b-versatile")


template = """You are a useful assistant.
Only answer the User Question:
{question}
"""
prompt = ChatPromptTemplate.from_template(template)


parser = StrOutputParser()
chain = prompt | model | parser
app = FastAPI(
    title="My LLM API",
    description="FastAPI-based LLM API with memory using LangServe",
    version="1.0",
)

add_routes(app, chain, path="/qa")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
