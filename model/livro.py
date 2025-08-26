from model.autor import Autor
from model.categoria import Categoria
from model.editora import Editora


class Livro:
    id_livros = 1  # Gerador de IDs de Autores

    __slots__ = ['__id', '__titulo', '__ano', '__paginas', '__isbn', '__resumo', '__autor', '__categoria', '__editora',]

    def __init__(self, titulo: str, ano: int, paginas: int, isbn: str, resumo: str):
        self.id = Livro.id_livros
        self.titulo = titulo
        self.ano = ano
        self.paginas = paginas
        self.isbn = isbn
        self.resumo = resumo
        self.__autor = None
        self.__categoria = None
        self.__editora = None

    def __str__(self):
        return f"{self.id} | {self.titulo} | {self.ano} | {self.paginas} | {self.isbn} | {self.autor.nome} | {self.categoria.nome} | {self.editora.nome}"

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, i: int) -> None:
        self.__id = i
        Livro.id_livros += 1

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, t: str) -> None:
        self.__titulo = t

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, a: int) -> None:
        self.__ano = a

    @property
    def paginas(self) -> int:
        return self.__paginas

    @paginas.setter
    def paginas(self, p: int) -> None:
        self.__paginas = p

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, i: str) -> None:
        self.__isbn = i

    @property
    def resumo(self) -> str:
        return self.__resumo

    @resumo.setter
    def resumo(self, r: str) -> None:
        self.__resumo = r

    @property
    def autor(self) -> Autor:
        return self.__autor

    @autor.setter
    def autor(self, a: Autor) -> None:
        self.__autor = a

    @property
    def categoria(self) -> Categoria:
        return self.__categoria

    @categoria.setter
    def categoria(self, c: Categoria) -> None:
        self.__categoria = c

    @property
    def editora(self) -> Editora:
        return self.__editora

    @editora.setter
    def editora(self, e: Editora) -> None:
        self.__editora = e

