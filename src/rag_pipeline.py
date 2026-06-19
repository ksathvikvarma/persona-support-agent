import os
from pypdf import PdfReader


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


if __name__ == "__main__":

    docs = load_documents()

    print(f"\nLoaded {len(docs)} documents\n")

    for doc in docs:

        print("=" * 60)
        print("SOURCE:", doc["source"])
        print()
        print(doc["content"][:300])
        print()