# main.py

import sys
from app.ingestion import ingest_documents
from app.query import query_documents


def print_help():
    """
    Exibe informações de ajuda do sistema, listando todos os comandos disponíveis.
    """
    print("\nSistema RAG com Ollama")
    print("-" * 30)
    print("Comandos disponíveis:")
    print("  ingest     - Indexa documentos da pasta data/")
    print("  query      - Realiza uma consulta")
    print("  help       - Mostra esta ajuda")
    print("  exit       - Sai do programa")


def main():
    """
    Função principal do sistema RAG com Ollama.
    
    Permite dois modos de operação:
    1. Modo de linha de comando: processar argumentos passados via sys.argv
    2. Modo interativo: interface de terminal para comandos contínuos
    
    Os comandos suportados são:
    - ingest: para indexar documentos
    - query: para consultar o sistema
    - help: para exibir a ajuda
    - exit: para sair do programa (apenas no modo interativo)
    """
    if len(sys.argv) > 1:
        # Command line arguments mode
        command = sys.argv[1].lower()
        
        if command == "ingest":
            ingest_documents()
        elif command == "query" and len(sys.argv) > 2:
            query = " ".join(sys.argv[2:])
            result = query_documents(query)
            print("\nResposta:", result)
        else:
            print_help()
    else:
        # Interactive mode
        print("\nBem-vindo ao Sistema RAG com Ollama")
        print("Digite 'help' para ver os comandos disponíveis")
        
        while True:
            try:
                command = input("\n> ").strip().lower()
                
                if command == "help":
                    print_help()
                elif command == "ingest":
                    ingest_documents()
                elif command.startswith("query "):
                    query = command[6:].strip()
                    if query:
                        result = query_documents(query)
                        print("\nResposta:", result)
                    else:
                        print("Por favor, forneça uma consulta.")
                elif command == "exit":
                    print("Saindo...")
                    break
                else:
                    print("Comando não reconhecido. Digite 'help' para ver os comandos disponíveis.")
            except KeyboardInterrupt:
                print("\nSaindo...")
                break
            except Exception as e:
                print(f"Erro: {e}")


if __name__ == "__main__":
    main()