from langchain.text_splitter import RecursiveCharacterTextSplitter

documents = [
    "Computer Science is the study of computers and computational systems.",
    "Artificial Intelligence enables machines to perform tasks that normally require human intelligence.",
    "RAG combines information retrieval with language generation."
]

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = []
for doc in documents:
    chunks.extend(splitter.split_text(doc))

print("Document Chunks:")
for chunk in chunks:
    print("-", chunk)

question = "What is RAG?"

for chunk in chunks:
    if "RAG" in chunk:
        print("\nAnswer:")
        print(chunk)
        break
