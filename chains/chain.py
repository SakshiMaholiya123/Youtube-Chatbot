from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from llm.llm import get_llm
from prompts.prompt import get_prompt
from retrievers.retriever import get_retriever


def format_docs(docs: list[Document]) -> str:
    formatted_docs = []

    for doc in docs:

        formatted_docs.append(
            f"""
Video Title: {doc.metadata.get("title")}

Channel Name: {doc.metadata.get("channel_title")}

Published At: {doc.metadata.get("published_at")}

Duration: {doc.metadata.get("duration")}

Views: {doc.metadata.get("view_count")}

Likes: {doc.metadata.get("like_count")}

Transcript:
{doc.page_content}
"""
        )

    return "\n\n".join(formatted_docs)


def get_rag_chain():
    """
    Build and return the RAG chain.
    """

    retriever = get_retriever()
    prompt = get_prompt()
    llm = get_llm()

    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain