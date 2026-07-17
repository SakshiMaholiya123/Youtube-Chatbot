from langchain_chroma import Chroma
from langchain_core.documents import Document

from config.settings import (
    CHROMA_DB_PATH,
    COLLECTION_NAME,
)

from embeddings.embedding_model import get_embedding_model


def create_vectorstore(documents: list[Document]) -> Chroma:

    embedding_model = get_embedding_model()

    # Load collection
    vectorstore = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embedding_model,
        collection_name=COLLECTION_NAME,
    )

    # Delete previous collection if it exists
    try:
        vectorstore.delete_collection()
        print("Previous collection deleted.")
    except Exception:
        print("No previous collection found.")

    # Create a fresh collection
    vectorstore = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embedding_model,
        collection_name=COLLECTION_NAME,
    )

    BATCH_SIZE = 50

    for i in range(0, len(documents), BATCH_SIZE):

        batch = documents[i:i + BATCH_SIZE]

        print(f"Processing batch {i} to {i + len(batch)}")

        vectorstore.add_documents(batch)

    return vectorstore


def load_vectorstore() -> Chroma:
    embedding_model = get_embedding_model()

    return Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embedding_model,
        collection_name=COLLECTION_NAME,
    )