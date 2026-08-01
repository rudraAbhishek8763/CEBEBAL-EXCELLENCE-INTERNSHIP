import os

from dotenv import load_dotenv
import google.generativeai as genai

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# -----------------------------
# Configuration
# -----------------------------
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL = genai.GenerativeModel("gemini-flash-latest")

DB_PATH = "vector_db"


# -----------------------------
# Load Vector Database
# -----------------------------
def load_vector_store():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )


# -----------------------------
# Retrieve Context
# -----------------------------
def retrieve_context(vector_store, question, k=4):

    docs = vector_store.similarity_search(question, k=k)

    context = "\n\n".join(doc.page_content for doc in docs)

    return context


# -----------------------------
# Generate Answer
# -----------------------------
def ask_gemini(question, context):

    prompt = f"""
You are an AI assistant helping users understand a document.

Use ONLY the information available in the context.

If the answer cannot be found, simply reply:

I couldn't find the answer in this document.

Context:
{context}

Question:
{question}

Answer:
"""

    response = MODEL.generate_content(prompt)

    return response.text


# -----------------------------
# Main Program
# -----------------------------
def main():

    print("=" * 60)
    print("📄 Document Question Answering System")
    print("Type 'exit' to quit.")
    print("=" * 60)

    vector_store = load_vector_store()

    while True:

        question = input("\nQuestion : ").strip()

        if question.lower() in ["exit", "quit"]:
            print("\nGoodbye!")
            break

        if not question:
            print("Please enter a question.")
            continue

        context = retrieve_context(vector_store, question)

        answer = ask_gemini(question, context)

        print("\nAnswer")
        print("-" * 50)
        print(answer)


if __name__ == "__main__":
    main()