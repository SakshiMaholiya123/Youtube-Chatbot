from indexing.document_ingestion import ingest_document
from processing.splitter import split_documents

from vectorstore.chroma_store import create_vectorstore
from chains.chain import get_rag_chain


def process_video(url: str):
    
    # Document ingestion
    documents = ingest_document(url)

    # Text splitting
    chunks = split_documents(documents)

    # Create vector store
    vectorstore = create_vectorstore(chunks)

    return vectorstore


def ask_question(question: str):

    rag_chain = get_rag_chain()

    response = rag_chain.invoke(question)

    return response