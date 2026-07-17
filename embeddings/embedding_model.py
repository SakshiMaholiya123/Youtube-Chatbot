import os

from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings

from config.settings import EMBEDDING_MODEL

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")


def get_embedding_model() -> CohereEmbeddings:
   
    if not COHERE_API_KEY:
        raise ValueError("COHERE_API_KEY not found in .env file")

    embeddings = CohereEmbeddings(
        model=EMBEDDING_MODEL,
        cohere_api_key=COHERE_API_KEY,
    )

    return embeddings