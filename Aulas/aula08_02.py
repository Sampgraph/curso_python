class Autor:
    __slots__ = ['nome', 'email', 'telefone', 'biografia']  # Bloqueia os objetos da classe para não adicionarem novos atributos.

    def __init__(self):  # Método construtor
        self.nome = None
        self.email = None
        self.telefone = None
        self.biografia = None


a = Autor()
a.nome = 'Machado de assis'
a.email = 'machado@teste.com'
a.telefone = '1234-5678'
a.biografia = 'Biografia do autor'


print(a.nome)  # Se fosse um dict seria a.get('nome')
print(a.email)  # Se fosse um dict seria a.get('email')
print(a.telefone)  # Se fosse um dict seria a.get('telefone')
print(a.biografia)  # Se fosse um dict seria a.get('biografia')

print('*' * 80)

b = Autor()
b.name = 'Cecília Meireles'  # Agora o Python não vai aceitar isso.
b.e_mail = 'meireles@teste.com'  # Agora o Python não vai aceitar isso.

print(b.nome)
print(b.email)
print(b.name)
print(b.e_mail)
