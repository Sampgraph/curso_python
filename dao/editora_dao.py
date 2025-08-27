from model.editora import Editora

class EditoraDAO:
    __tabela_editoras = []  # Atributo de classe representando a tabela de Editoras.

    # Métodos CRUD

    def create(self, editora: Editora) -> None:
        EditoraDAO.__tabela_editoras.append(editora)

    def read(self, editora_id) -> Editora:
        for editora in EditoraDAO.__tabela_editoras:
            if (editora.id == editora_id):
                return editora

        # Se chegar até nessa linha significa que a editora não foi encontrada.
        raise IndexError('Editora não encontrada')

    def update(self, id: int, editora: Editora):
        for index, editora in enumerate(EditoraDAO.__tabela_editoras):
            if editora.id == id:
                EditoraDAO.__tabela_editoras[index] = editora
                return

    def delete(self, editora_id: int) -> bool:
        for index, editora in enumerate(EditoraDAO.__tabela_editoras):
            if editora.id == editora_id:
                encontrado = True
                break

        # Se chegar até nessa linha significa que a editora não foi encontrada.
        raise IndexError('Editora não encontrada')

    def read_all(self) -> list:
        return EditoraDAO.__tabela_editoras

    def is_empty(self) -> bool:
        return len(EditoraDAO.__tabela_editoras) == 0

