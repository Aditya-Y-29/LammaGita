from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders.csv_loader import CSVLoader
import pandas as pd

CHUNK_SIZE= 250
CHUNK_OVERLAP= 50
DATA_PATH= 'data/'
DB_FAISS_PATH= 'vectorstore/db_faiss'


# Build vector database
def run_db_build():
    
    loader = CSVLoader(file_path='data/dataset.csv', csv_args={
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ['Learning','Meaning']})
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE,
                                                   chunk_overlap=CHUNK_OVERLAP)
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                       model_kwargs={'device': 'cpu'})

    vectorstore = FAISS.from_documents(texts, embeddings)
    vectorstore.save_local(DB_FAISS_PATH)

if __name__ == "__main__":
    run_db_build()