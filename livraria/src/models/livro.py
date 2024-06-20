class Livro:
    def __init__(self, id, nome, titulo, autor, sinopse):
        
        self.__id = id
        self.__nome = nome
        self.__titulo = titulo
        self.__autor = autor
        self.__sinopse = sinopse
    
    #getts
    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_sinopse(self):
        return self.__sinopse
    
    #setters
    def set_id(self, id):
         self.__id = id
    
    def set_nome(self, nome):
         self.__nome = nome
   
    def set_titulo(self, titulo):
         self.__titulo = titulo
    
    def set_autor(self, autor):
         self.__autor = autor
        
    
    def set_sinopse(self, sinopse):
         self.__sinopse = sinopse

    def __str__(self):

        return f"ID: {self.__id}, Nome: {self.__nome}, Titulo: {self.__titulo}, Autor: {self.__autor}, Sinopse: {self.__sinopse}"