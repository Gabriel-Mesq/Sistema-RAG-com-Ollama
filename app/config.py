# app/config.py

from pathlib import Path
from pydantic_settings import BaseSettings  


class Settings(BaseSettings):
    DOCUMENTS_PATH: str = "data"
    VECTOR_STORE_PATH: str = "vector_store/faiss_index"
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 50
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"  
    LLM_MODEL: str = "llama3.2"

    class Config:
        env_file = ".env"


settings = Settings()
print("Módulo de configurações executado com sucesso.")