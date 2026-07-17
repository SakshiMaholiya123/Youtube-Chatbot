from langchain_core.vectorstores import VectorStoreRetriever

from config.settings import (
    SEARCH_TYPE,
    TOP_K_RESULTS,
)

from vectorstore.chroma_store import load_vectorstore


def get_retriever() -> VectorStoreRetriever:
   

    vectorstore = load_vectorstore()

    retriever = vectorstore.as_retriever(
        search_type=SEARCH_TYPE,
        search_kwargs={
            "k": TOP_K_RESULTS,
        },
    )

    return retriever