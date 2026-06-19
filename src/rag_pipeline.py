import os
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

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
        chunk_size=300,
        chunk_overlap=50
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

if __name__ == "__main__":

    docs = load_documents()

    chunks = chunk_documents(docs)

    print(f"\nTotal Chunks: {len(chunks)}\n")

    for chunk in chunks[:5]:

        print("=" * 60)
        print("SOURCE:", chunk["source"])
        print("CHUNK:", chunk["chunk_index"])
        print()
        print(chunk["text"])
        print()