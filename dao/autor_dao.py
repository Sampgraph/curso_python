from model.autor import Autor


class AutorDAO:
    __tabela_autores = [] # Atributo de classe representando a tabela de Autores.

    # Métodos CRUD

    def create(self, autor: Autor):
        AutorDAO.__tabela_autores.append(autor)

    def read(self, id: int):
        for autor in AutorDAO.__tabela_autores:
            if autor.id == id:
                return autor

        # Se chegar até nessa linha significa que o autor não foi encontrado.
        raise IndexError('Autor não encontrado')

    def update(self, id: int, autor: Autor):
        for index, autor in enumerate(AutorDAO.__tabela_autores):
            if autor.id == id:
                AutorDAO.__tabela_autores[index] = autor
                return

    def delete(self, id: int):
        for autor in AutorDAO.__tabela_autores:
            if autor.id == id:
                AutorDAO.__tabela_autores.remove(autor)
                return

        # Se chegar até nessa linha significa que o autor não foi encontrado.
        raise IndexError('Autor não encontrado')

    def read_all(self) -> list:  # Listar todos os registros
        return AutorDAO.__tabela_autores


    def is_empty(self) -> bool:
        return len(AutorDAO.__tabela_autores) == 0

