!pip -q install langchain langchain-community langchain-huggingface langchain-groq sentence-transformers faiss-cpu pypdf

import os
from google.colab import files

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ["GROQ_API_KEY"] = "YOUR_GROQ_API_KEY_HERE"

uploaded = files.upload()
pdf_file = list(uploaded.keys())[0]

loader = PyPDFLoader(pdf_file)
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

print(f"Loaded {len(documents)} pages")
print(f"Created {len(chunks)} chunks")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(chunks, embeddings)

retriever = vectorstore.as_retriever(
    search_kwargs={"k":5}
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
You are an AI assistant answering questions ONLY from the uploaded document.

Rules:
- Answer only using the provided context.
- If the answer is not present, reply:
  "I could not find the answer in the uploaded document."
- Do not make up information.

Context:
{context}

Question:
{question}

Answer:
""")

parser = StrOutputParser()

chain = prompt | llm | parser

def ask(question):
    docs = retriever.invoke(question)
    context = "\n\n".join(doc.page_content for doc in docs)
    return chain.invoke({
        "context": context,
        "question": question
    })

print("RAG Ready!")

while True:
    question = input("\nQuestion: ")

    if question.lower() == "exit":
        break

    answer = ask(question)

    print("\nAnswer:\n")
    print(answer)