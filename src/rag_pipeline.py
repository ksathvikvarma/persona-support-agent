import os

import chromadb
from dotenv import load_dotenv
from google import genai
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader

from config import (CHUNK_SIZE, CHUNK_OVERLAP,COLLECTION_NAME,CHROMA_DB_PATH,TOP_K_RESULTS,EMBEDDING_MODEL)
    

def load_documents(data_folder="data"):
    documents = []

    for filename in os.listdir(data_folder):

        filepath = os.path.join(data_folder, filename)

        # TXT and Markdown files
        if filename.endswith(".txt") or filename.endswith(".md"):

            with open(filepath, "r", encoding="utf-8") as file:

                text = file.read()

                documents.append(
                    {
                        "source": filename,
                        "content": text
                    }
                )

        # PDF files
        elif filename.endswith(".pdf"):

            pdf_text = ""

            reader = PdfReader(filepath)

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    pdf_text += page_text + "\n"

            documents.append(
                {
                    "source": filename,
                    "content": pdf_text
                }
            )

    return documents

def chunk_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    all_chunks = []

    for doc in documents:

        chunks = splitter.split_text(doc["content"])

        for index, chunk in enumerate(chunks):

            all_chunks.append(
                {
                    "text": chunk,
                    "source": doc["source"],
                    "chunk_index": index
                }
            )

    return all_chunks

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def get_embedding(text):
    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text
    )

    return response.embeddings[0].values

def create_vector_db(chunks):

    chroma_client = chromadb.PersistentClient(
        path=CHROMA_DB_PATH
    )

    try:
        chroma_client.delete_collection(COLLECTION_NAME)
    except:
        pass

    collection = chroma_client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    for i, chunk in enumerate(chunks):

        embedding = get_embedding(chunk["text"])

        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[chunk["text"]],
            metadatas=[
                {
                    "source": chunk["source"],
                    "chunk_index": chunk["chunk_index"]
                }
            ]
        )

    return collection

def get_collection():

    chroma_client = chromadb.PersistentClient(
        path=CHROMA_DB_PATH
    )

    collection = chroma_client.get_collection(
        name=COLLECTION_NAME
    )

    return collection

def retrieve_documents(query, collection, top_k=TOP_K_RESULTS):

    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results

# if __name__ == "__main__":

#     docs = load_documents()

#     chunks = chunk_documents(docs)

#     print(f"\nTotal Chunks: {len(chunks)}\n")

#     for chunk in chunks[:5]:

#         print("=" * 60)
#         print("SOURCE:", chunk["source"])
#         print("CHUNK:", chunk["chunk_index"])
#         print()
#         print(chunk["text"])
#         print()

if __name__ == "__main__":

    docs = load_documents()

    chunks = chunk_documents(docs)

    collection = create_vector_db(chunks)

    results = retrieve_documents(
        "How do I reset my password?",
        collection
    )

    print("\nRETRIEVED RESULTS\n")

    for doc in results["documents"][0]:

        print("=" * 50)
        print(doc)
        print()