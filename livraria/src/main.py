from src.database.crud import create_table,add_livro,get_livro, update_livro
from src.utils import validade_book_data

def main():
    create_table()

    while True:

        print("\nGERENCIADOR DE LIVROS")
        print("1 Adicionar livro: ")
        print("2 Listar livro: ")
        print("3 Atualizar livro: ")
        print("4 Deletar livro: ")
        print("5 sair ")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input ("Nome: ")
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            sinopse = input("Sinopse")
            valid, message = validade_book_data(nome, titulo, autor, sinopse)
            if valid:
                add_livro(nome, titulo, autor,sinopse)
                print("Este livro foi adicionado com sucesso!")
            else:
                print(f"erro: {message}")
        elif escolha == '2':
            books = get_books()
            for book in books:
                print(book)
        elif escolha == '3':
            id = int(input("ID do livro a ser atualizado: "))
            nome = input("Novo Nome: ")
            titulo = input("Novo Título: ")
            autor = input("Novo Autor: ")
            sinopse = input("Nova Sinopse: ")
            valid, message = validate_book_data(nome, titulo, autor, sinopse)
            if valid:
                update_book(id, nome, titulo, autor, sinopse)
                print("Livro atualizado com sucesso!")
            else:
                print(f"Erro: {message}")
        elif escolha == '4':
            id = int(input("ID do livro a ser deletado: "))
            delete_book(id)
            print("Livro deletado com sucesso!")
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()



    