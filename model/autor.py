from model.utils import is_email_valid


class Autor:
    id_autores = 1  # Gerador de IDs de Autores

    __slots__ = ['__id', '__nome', '__email', '__telefone', '__biografia']

    def __init__(self, n: str, t: str, b: str =None) -> None:  # Método construtor
        self.id = Autor.id_autores
        self.nome = n
        self.__email = None  # Convenção para definir um atributo como 'protegido'.
        self.telefone = t
        self.biografia = b

    def __str__(self) -> str:
        return f"{self.id} | {self.__nome} | {self.__email} | {self.__telefone}"

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, i: int) -> None:
        self.__id = i
        Autor.id_autores += 1

    @property  # Decorator ou decoradores
    def nome(self) -> str:
        return self.__nome

    @nome.setter  # Decorator ou decoradores
    def nome(self, n: str) -> None:
        self.__nome = n.title()

    @property  # Decorator ou decoradores
    def email(self) -> str:
        return self.__email

    @email.setter  # Decorator ou decoradores
    def email(self, e: str) -> None:
        if is_email_valid(e):
            self.__email = e.lower()
            return
        else:
            raise ValueError('Email inválido')

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, t: str) -> None:
        self.__telefone = t

    @property
    def biografia(self) -> str:
        return self.__biografia

    @biografia.setter
    def biografia(self, b: str) -> None:
        self.__biografia = b

