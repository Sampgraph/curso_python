from model.autor import Autor


class AutorDAO:
    tabela_autores = [] # Atributo de classe representando a tabela de Autores.

    # Métodos CRUD

    def create(self, autor: Autor):
        AutorDAO.tabela_autores.append(autor)

    def read(self, id: int):
        return AutorDAO.tabela_autores[id]

    def update(self, id: int, autor: Autor):
        AutorDAO.tabela_autores[id] = autor

    def delete(self, id: int):
        AutorDAO.tabela_autores.pop(id)

    def read_all(self) -> list:  # Listar todos os registros
        return AutorDAO.tabela_autores


