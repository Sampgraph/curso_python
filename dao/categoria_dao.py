from model.categoria import Categoria

class CategoriaDAO:
    __tabela_categorias = []  # Atributo de classe representando a tabela de Categorias.

    # Métodos CRUD

    def create(self, categoria: Categoria) -> None:  # INSERT INTO categoria
        CategoriaDAO.__tabela_categorias.append(categoria)

    def read(self, categoria_id) -> Categoria:
        for categoria in CategoriaDAO.__tabela_categorias:
            if categoria.id == categoria_id:
                return categoria

        # Se chegar até nessa linha significa que a categoria não foi encontrada.
        raise IndexError('Categoria não encontrada')

    def update(self, id: int, categoria: Categoria):
        for index, categoria in enumerate(CategoriaDAO.__tabela_categorias):
            if categoria.id == id:
                CategoriaDAO.__tabela_categorias[index] = categoria
                return

    def delete(self, categoria_id: int) -> bool:
        for index, categoria in enumerate(CategoriaDAO.__tabela_categorias):
            if categoria.id == categoria_id:
                CategoriaDAO.__tabela_categorias.pop(index)
                return

        # Se chegar até nessa linha significa que a categoria não foi encontrada.
        raise IndexError('Categoria não encontrada')

    def read_all(self) -> list:  # SELECT * FROM categoria
        return CategoriaDAO.__tabela_categorias


    def is_empty(self) -> bool:
        return len(CategoriaDAO.__tabela_categorias) == 0

