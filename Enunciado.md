Desafio Técnico - Sistema RAG com Ollama

Contexto
Você foi contratado como desenvolvedor de IA em uma empresa que deseja implementar um sistema inteligente de atendimento ao cliente baseado em documentos internos. A ideia é permitir que os usuários façam perguntas sobre documentos institucionais e recebam respostas contextualizadas geradas por um modelo de linguagem natural.

Seu desafio é construir um sistema funcional de geração aumentada por recuperação (RAG), capaz de indexar documentos, realizar buscas semânticas e gerar respostas usando um modelo local via Ollama. O foco está na aplicação prática, na organização do código e no uso de boas práticas de engenharia de software.

Objetivo
Criar um sistema simples de Pergunta e Resposta (QA) utilizando o paradigma RAG (Retrieval-Augmented Generation). O sistema deve permitir ao usuário fazer perguntas sobre documentos, usando um modelo local via Ollama e banco vetorial.

Requisitos
1. Ingestão de Documentos:
Aceitar arquivos .txt ou .md

Dividir textos em chunks configuráveis

Indexar com FAISS, Chroma, etc.

2. Busca Vetorial:
Buscar chunks semanticamente relevantes

3. Integração com Ollama:
Usar modelo local (ex: llama2, mistral)

Concatenar contexto + pergunta no prompt

4. Interface:
CLI ou API simples

Modelos recomendados via Ollama
Modelos leves que funcionam em CPU:

mistral

llama2:7b

gemma:2b

Ollama roda em CPU! Não requer GPU. Exige ~8-16GB de RAM. Ver: https://ollama.com/library

Tempo Estimado
3 a 6 horas.

Entrega Esperada
Repositório (Git ou zip)

README com instruções

Exemplo de pergunta

(Opcional) Docker, Makefile, vídeo

Alternativa sem GPU
Pode usar API pública (OpenAI, Together.ai). Modularize o código. Documente essa escolha.