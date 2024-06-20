def validate_book_data(nome, titulo, autor, sinopse):
    if not nome or not titulo or not autor:
        return False, "Nome, Título e Autor são campos obrigatórios."
    if len(nome) > 100 or len(titulo) > 100 or len(autor) > 100:
        return False, "Nome, Título e Autor não podem ter mais de 100 caracteres."
    return True, ""
