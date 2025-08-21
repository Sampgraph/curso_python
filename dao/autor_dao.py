from model.autor import Autor


class AutorDAO:
    tabela_autores = [] # Atributo de classe representando a tabela de Autores.

    # Métodos CRUD

    def create(self, autor: Autor):
        AutorDAO.tabela_autores.append(autor)

    def read(self, id: int):
        for autor in AutorDAO.tabela_autores:
            if autor.id == id:
                return autor

        # Se chegar até nessa linha significa que o autor não foi encontrado.
        raise IndexError('Autor não encontrado')

    def update(self, id: int, autor: Autor):
        for index, autor in enumerate(AutorDAO.tabela_autores):
            if autor.id == id:
                AutorDAO.tabela_autores[index] = autor
                return

    def delete(self, id: int):
        for autor in AutorDAO.tabela_autores:
            if autor.id == id:
                AutorDAO.tabela_autores.remove(autor)
                return

        # Se chegar até nessa linha significa que o autor não foi encontrado.
        raise IndexError('Autor não encontrado')

    def read_all(self) -> list:  # Listar todos os registros
        return AutorDAO.tabela_autores

