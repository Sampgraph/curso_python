class Autor:
    __slots__ = ['__nome', '__email', '__telefone', '__biografia']  #
    # double underline slots double underline
    # dunder slots

    def __init__(self):  # Método construtor
        """ double underline init double underline
            dunder init
        """
        self.__nome = None
        self.__email = None
        self.__telefone = None
        self.__biografia = None

    def __str__(self):
        """ dunder str """
        return super().__str__()


a = Autor()
print(a)

