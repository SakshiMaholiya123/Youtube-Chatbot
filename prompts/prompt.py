from langchain_core.prompts import ChatPromptTemplate


def get_prompt() -> ChatPromptTemplate:
    """
    Create and return the RAG prompt template.

    Returns:
        ChatPromptTemplate
    """

    prompt = ChatPromptTemplate.from_template(
        """
You are a helpful AI assistant.

Your task is to answer the user's question ONLY using the provided context.

Instructions:
1. Answer only from the context.
2. Do not make up information.
3. If the answer is not available in the context, reply:
   "I couldn't find that information in the provided video transcript."
4. Keep the answer clear and concise.
5. If appropriate, explain the answer in simple language.

-----------------------------
Context:
{context}
-----------------------------

Question:
{question}

Answer:
"""
    )

    return prompt