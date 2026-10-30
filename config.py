import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_llm():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY missing in .env")

    return ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.2,
        max_tokens=2048,
        api_key=api_key
    )

llm = get_llm()