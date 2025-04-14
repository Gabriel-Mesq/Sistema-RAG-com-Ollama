# app/ingestion.py

import os
from pathlib import Path
from typing import List

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.docstore.document import Document

from app.config import settings


def load_documents_from_folder(folder_path: str) -> List[Document]:
    """
    Carrega documentos de texto a partir de uma pasta.

    Args:
        folder_path (str): Caminho para a pasta contendo os documentos.

    Returns:
        List[Document]: Lista de documentos carregados.
    """
    docs = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith((".txt", ".md")):
            with open(os.path.join(folder_path, file_name), "r", encoding="utf-8") as f:
                text = f.read()
                docs.append(Document(page_content=text, metadata={"source": file_name}))
    return docs


def chunk_documents(documents: List[Document]) -> List[Document]:
    """
    Divide documentos em chunks menores para processamento.

    Args:
        documents (List[Document]): Lista de documentos a serem divididos.

    Returns:
        List[Document]: Lista de chunks gerados a partir dos documentos.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP
    )
    return splitter.split_documents(documents)


def index_documents(chunks: List[Document], persist_path: str) -> None:
    """
    Cria um índice vetorial a partir dos chunks de documentos e salva localmente.

    Args:
        chunks (List[Document]): Lista de chunks de documentos.
        persist_path (str): Caminho onde o índice será salvo.
    """
    embeddings = HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL)
    vectorstore = FAISS.from_documents(chunks, embedding=embeddings)
    vectorstore.save_local(persist_path)
    print(f"Índice salvo em: {persist_path}")


def ingest_documents() -> None:
    """
    Executa o pipeline completo de ingestão de documentos:
    carregamento, divisão em chunks e indexação.
    """
    print("🔍 Carregando documentos...")
    docs = load_documents_from_folder(settings.DOCUMENTS_PATH)
    print(f"📄 {len(docs)} documentos encontrados.")

    print("✂️ Dividindo em chunks...")
    chunks = chunk_documents(docs)
    print(f"🧩 {len(chunks)} chunks gerados.")

    print("💾 Indexando com FAISS...")
    index_documents(chunks, settings.VECTOR_STORE_PATH)
    print("✅ Ingestão concluída.")