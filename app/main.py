# main.py

import sys
from ingestion import ingest_documents
from query import query_documents

def print_help():
    print("\nSistema RAG com Ollama")
    print("-" * 30)
    print("Comandos disponíveis:")
    print("  ingest     - Indexa documentos da pasta data/")
    print("  query      - Realiza uma consulta")
    print("  help       - Mostra esta ajuda")
    print("  exit       - Sai do programa")

def main():
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