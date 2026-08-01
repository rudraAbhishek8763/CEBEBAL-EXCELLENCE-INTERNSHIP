import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


PDF_PATH = "data/Cryptographic Solutions.pdf"
DB_PATH = "vector_db"


def load_documents():
    loader = PyPDFLoader(PDF_PATH)
    return loader.load()


def split_into_chunks(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=80
    )
    return splitter.split_documents(documents)


def embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def create_vector_store(chunks):
    embeddings = embedding_model()
    return FAISS.from_documents(chunks, embeddings)


def main():

    print("=" * 50)
    print("Building Vector Database")
    print("=" * 50)

    docs = load_documents()
    print(f"Loaded {len(docs)} pages")

    chunks = split_into_chunks(docs)
    print(f"Created {len(chunks)} chunks")

    vector_store = create_vector_store(chunks)

    os.makedirs(DB_PATH, exist_ok=True)
    vector_store.save_local(DB_PATH)

    print("\nVector database saved successfully!")


if __name__ == "__main__":
    main()