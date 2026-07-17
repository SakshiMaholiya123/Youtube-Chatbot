import os
from functools import lru_cache

from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings

from config.settings import EMBEDDING_MODEL

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")


@lru_cache(maxsize=1)
def get_embedding_model() -> CohereEmbeddings:

    print("Loading Cohere Embedding Model...")

    if not COHERE_API_KEY:
        raise ValueError("COHERE_API_KEY not found in .env")

    return CohereEmbeddings(
        model=EMBEDDING_MODEL,
        cohere_api_key=COHERE_API_KEY,
    )