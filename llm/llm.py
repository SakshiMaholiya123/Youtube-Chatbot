import os
from functools import lru_cache

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

from config.settings import (
    LLM_MODEL,
    TEMPERATURE,
    MAX_TOKENS,
)

load_dotenv()


@lru_cache(maxsize=1)
def get_llm() -> ChatMistralAI:
   
    print("Loading Mistral LLM...")

    api_key = os.getenv("MISTRAL_API_KEY")

    if not api_key:
        raise ValueError("MISTRAL_API_KEY not found in .env")

    return ChatMistralAI(
        api_key=api_key,
        model=LLM_MODEL,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )