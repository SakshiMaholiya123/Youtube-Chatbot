from indexing.document_ingestion import ingest_document
from processing.splitter import split_documents

from vectorstore.chroma_store import create_vectorstore
from chains.chain import get_rag_chain


def process_video(url: str):
    # Document ingestion
    documents = ingest_document(url)

    # Split transcript
    chunks = split_documents(documents)

    # Create ChromaDB
    create_vectorstore(chunks)

    # Build RAG chain once
    rag_chain = get_rag_chain()

    return rag_chain


def ask_question(rag_chain, question: str):

    return rag_chain.invoke(question)