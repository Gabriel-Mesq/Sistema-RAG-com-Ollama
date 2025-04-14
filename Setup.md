# Tutorial de Instalação e Uso do Sistema RAG com Ollama

Este guia fornecerá instruções detalhadas para instalar e utilizar o Sistema RAG (Retrieval-Augmented Generation) com Ollama.

## Pré-requisitos

- Python 3.8 ou superior
- [Ollama](https://ollama.com/) instalado no seu sistema
- Pelo menos 8GB de RAM (recomendado 16GB)
- Git (opcional, para clonar o repositório)

## Instalação

### 1. Obtenha o código

```bash
git clone https://github.com/Gabriel-Mesq/Sistema-RAG-com-Ollama.git
cd Sistema-RAG-com-Ollama
```

Ou baixe e descompacte o arquivo ZIP do projeto.

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
```

**Windows**
```bash
venv\Scripts\activate
```

**Linux/Mac**
```bash
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Instale o modelo Llama3 no Ollama

```bash
ollama pull llama3.2
```

## Uso do Sistema

O sistema oferece duas funcionalidades principais: ingestão de documentos e consulta.

### 1. Ingestão de Documentos

Para indexar os documentos que estão na pasta `data/`, execute:

```bash
python -m app.main ingest
```

Este comando irá:
- Carregar todos os arquivos .txt e .md da pasta `data/`
- Dividir os documentos em chunks
- Gerar embeddings para cada chunk
- Armazenar os embeddings em um índice FAISS

### 2. Consulta ao Sistema

Há dois modos de fazer consultas:

**Modo linha de comando:**
```bash
python -m app.main query "Qual a remuneração de um colaborador responsavel pela arquitetura de soluções e mentoria técnica?"
```

**Modo interativo:**
```bash
python -m app.main
```

No modo interativo, você verá um prompt `>`. Digite seus comandos:
- `query Sua pergunta aqui` - Para fazer uma consulta
- `ingest` - Para reindexar os documentos
- `help` - Para exibir ajuda
- `exit` - Para sair do programa

## Adicionando Documentos

Para adicionar novos documentos ao sistema:

1. Coloque seus arquivos .txt ou .md na pasta `data/`
2. Execute o comando de ingestão novamente:
    ```bash
    python -m app.main ingest
    ```

## Exemplos de Consultas

- "Quais são os benefícios oferecidos aos colaboradores?"
- "Como funciona a política de reembolso para produtos de software?"
- "Qual é a história da empresa?"
- "Quem fundou a Nonsense Solver?"
- "Qual a remuneração de um colaborador responsavel pela arquitetura de soluções e mentoria técnica?"

## Solução de Problemas

### O índice não foi criado
Verifique se você executou o comando `ingest` antes de fazer consultas.

### Erros com o Ollama
Certifique-se de que o Ollama está em execução e que você baixou o modelo `llama3.2`.

### Problemas de memória
Se encontrar erros de memória, tente:
- Fechar aplicativos que consomem muita RAM
- Modificar o tamanho do chunk em `app/config.py` para um valor menor

## Personalização

Você pode ajustar as configurações do sistema editando o arquivo `app/config.py`:

- `CHUNK_SIZE`: Tamanho dos chunks (padrão: 500)
- `CHUNK_OVERLAP`: Sobreposição entre chunks (padrão: 50)
- `EMBEDDING_MODEL`: Modelo para embeddings (padrão: "all-MiniLM-L6-v2")
- `LLM_MODEL`: Modelo LLM para respostas (padrão: "llama3.2")