from crud import create_table, add_book, get_books, update_book, delete_book
from utils import validate_book_data
from book import Book  # Adicione esta linha para verificar a importação

def main():
    create_table()

    while True:
        print("\nGerenciador de Livros")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Atualizar Livro")
        print("4. Deletar Livro")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            sinopse = input("Sinopse: ")
            valid, message = validate_book_data(nome, titulo, autor, sinopse)
            if valid:
                add_book(nome, titulo, autor, sinopse)
                print("Livro adicionado com sucesso!")
            else:
                print(f"Erro: {message}")
        elif escolha == '2':
            try:
                books = get_books()
                if books:
                    print("\nLista de Livros:")
                    for book in books:
                        print(book)
                else:
                    print("Nenhum livro encontrado.")
            except Exception as e:
                print(f"Erro ao listar livros: {e}")
        elif escolha == '3':
            id = input("ID do livro a ser atualizado: ")
            nome = input("Novo Nome: ")
            titulo = input("Novo Título: ")
            autor = input("Novo Autor: ")
            sinopse = input("Nova Sinopse: ")
            valid, message = validate_book_data(nome, titulo, autor, sinopse)
            if valid:
                try:
                    update_book(int(id), nome, titulo, autor, sinopse)
                    print("Livro atualizado com sucesso!")
                except Exception as e:
                    print(f"Erro ao atualizar livro: {e}")
            else:
                print(f"Erro: {message}")
        elif escolha == '4':
            id = input("ID do livro a ser deletado: ")
            try:
                delete_book(int(id))
                print("Livro deletado com sucesso!")
            except Exception as e:
                print(f"Erro ao deletar livro: {e}")
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    # Teste de instância da classe Book
    try:
        test_book = Book(1, "Nome Teste", "Título Teste", "Autor Teste", "Sinopse Teste")
        print(test_book)
    except TypeError as e:
        print(f"Erro ao instanciar Book: {e}")

    main()
