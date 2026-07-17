from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from retrievers.retriever import get_retriever
from prompts.prompt import get_prompt
from llm.llm import get_llm


def format_docs(docs):
    
    return "\n\n".join(
        doc.page_content for doc in docs
    )


def get_rag_chain():
    
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