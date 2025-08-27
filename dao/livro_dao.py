class LivroDAO:
    __tabela_livros = []

    # Métodos CRUD

    def create(self, livro):
        self.__tabela_livros.append(livro)

    def read(self, livro_id):
        for livro in self.__tabela_livros:
            if livro.id == livro_id:
                return livro

        # Se chegar até nessa linha significa que o livro não foi encontrado.
        raise IndexError("Livro não encontrado")

    def update(self, livro_id, livro):
        for i, livro in enumerate(self.__tabela_livros):
            if livro.id == livro_id:
                self.__tabela_livros[i] = livro
                return

        # Se chegar até nessa linha significa que o livro não foi encontrado.
        raise IndexError("Livro não encontrado")

    def delete(self, livro_id):
        for i, livro in enumerate(self.__tabela_livros):
            if livro.id == livro_id:
                del self.__tabela_livros[i]
                return

        # Se chegar até nessa linha significa que o livro não foi encontrado.
        raise IndexError("Livro não encontrado")

    def read_all(self):
        return self.__tabela_livros

    def is_empty(self):
        return len(self.__tabela_livros) == 0

