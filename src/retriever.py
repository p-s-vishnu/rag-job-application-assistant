import os
import sys
from langchain.document_loaders import PDFPlumberLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings


def load_cv(FILE_PATH):
    if not os.path.exists(FILE_PATH):
        print("\nPath not found!!!")
        sys.exit(0)

    cv_loader = PDFPlumberLoader(FILE_PATH)
    return cv_loader


def create(FILE_PATH):
    cv_loader = load_cv(FILE_PATH)
    # print(cv_loader.load())
    # Split documents
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, 
                                                   chunk_overlap=50)
    splits = text_splitter.split_documents(cv_loader.load())

    # Embed and store splits
    vectorstore = Chroma.from_documents(documents=splits, 
                                        embedding=OpenAIEmbeddings())
    return vectorstore.as_retriever()
