import os

import streamlit as st
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
# Load FAISS Only Once
# -----------------------------
@st.cache_resource
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
def retrieve_context(vector_store, question):

    docs = vector_store.similarity_search(question, k=4)

    return "\n\n".join(doc.page_content for doc in docs)


# -----------------------------
# Gemini Response
# -----------------------------
def generate_answer(question, context):

    prompt = f"""
You are an assistant that answers questions only using the supplied document.

If the answer is unavailable, reply:

"I couldn't find the answer in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = MODEL.generate_content(prompt)

    return response.text


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(
    page_title="Document QA",
    page_icon="📄"
)

st.title("📄 RAG Document Question Answering")

st.write(
    "Ask questions about the uploaded PDF using semantic search and Gemini."
)

question = st.text_input("Enter your question")

if st.button("Get Answer"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        try:

            with st.spinner("Searching document..."):

                db = load_vector_store()

                context = retrieve_context(db, question)

                answer = generate_answer(question, context)

            st.success("Answer Generated")

            st.markdown("### Answer")

            st.write(answer)

        except Exception as e:

            st.error(e)