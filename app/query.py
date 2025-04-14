# app/query.py

import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM  # Classe atualizada

from app.config import settings

def query_documents(query_text: str) -> str:
    # Verificar se o índice existe
    if not os.path.exists(settings.VECTOR_STORE_PATH):
        return "O índice de documentos não foi criado. Execute 'ingest' primeiro."
    
    try:
        # Carregar embeddings e vectorstore
        print("🔍 Carregando modelo de embeddings...")
        embeddings = HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL)
        
        print("📚 Carregando índice de documentos...")
        vectorstore = FAISS.load_local(
            settings.VECTOR_STORE_PATH, 
            embeddings, 
            allow_dangerous_deserialization=True
        )
        
        # Buscar documentos relevantes
        print("🔎 Buscando documentos relevantes...")
        docs = vectorstore.similarity_search(query_text, k=2)
        
        # Preparar contexto para o modelo
        context = "\n\n".join([doc.page_content for doc in docs])
        
        # Criar o modelo de linguagem
        print("🤖 Consultando modelo de linguagem...")
        llm = OllamaLLM(model="llama3.2")  # Usando o modelo llama3.2 que você já baixou
        
        # Montar o prompt
        prompt = ChatPromptTemplate.from_template(
            """Você é um assistente de atendimento especializado em documentos corporativos.
            Responda à pergunta com base apenas no contexto fornecido.
            Se a informação não estiver no contexto, diga "Não encontrei essa informação nos documentos disponíveis.".
            
            Contexto:
            {context}
            
            Pergunta: {query}
            
            Resposta:"""
        )
        
        # Montar a cadeia de processamento
        chain = prompt | llm | StrOutputParser()
        
        # Executar a cadeia
        response = chain.invoke({"context": context, "query": query_text})
        
        return response
    
    except Exception as e:
        return f"Erro ao processar a consulta: {str(e)}"