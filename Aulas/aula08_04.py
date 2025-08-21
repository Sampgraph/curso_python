class Autor:
    __slots__ = ['__nome', '__email', '__telefone', '__biografia']  #

    def __init__(self, n, e, t, b):  # Método construtor
        """ double underline init double underline
            dunder init
        """
        self.__nome = n
        self.__email = e
        self.__telefone = t
        self.__biografia = b

    def __str__(self):  # é o equivalente a um método 'to_string'.
        return f"{self.__nome} | {self.__email} | {self.__telefone}"


a = Autor('machado', 'machado@teste.com', '1234-5678', 'Biografia do autor')
print(a)

