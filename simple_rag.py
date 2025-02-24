from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.document_loaders import WebBaseLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain import hub
from dotenv import load_dotenv
from typing import List
import os
import bs4

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key = os.getenv("GEMINI_API_KEY"))

loader = WebBaseLoader(
    web_paths=("https://medium.com/kodcular/llm-large-language-models-nedir-b%C3%BCy%C3%BCk-dil-modellerine-k%C4%B1sa-bir-giri%C5%9F-9872ce8523af",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("l")
        )
    ),
)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(
    documents=splits, 
    embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))

retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")



def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

if __name__ == "__main__":
    while True:
        user_input = input("\n --> Sormak istediğiniz soruyu yazınız ? ")
        
        if(user_input == 'q'):
            break
        
        for chunk in rag_chain.stream(user_input):
            print(chunk, end="", flush=True)
        
        