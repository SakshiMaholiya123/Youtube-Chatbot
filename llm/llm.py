import os

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

from config.settings import (
    LLM_MODEL,
    TEMPERATURE,
    MAX_TOKENS,
)

load_dotenv()


def get_llm() -> ChatMistralAI:

    api_key = os.getenv("MISTRAL_API_KEY")

    if not api_key:
        raise ValueError("MISTRAL_API_KEY not found in .env")

    llm = ChatMistralAI(
        api_key=api_key,
        model=LLM_MODEL,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )

    return llm