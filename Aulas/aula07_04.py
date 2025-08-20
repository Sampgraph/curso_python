class Autor:
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
b.name = 'Cecília Meireles'  # O Python aceita isso mas é fortemente desaconselhável.
b.e_mail = 'meireles@teste.com'  # O Python aceita isso mas é fortemente desaconselhável.

print(b.nome)
print(b.email)
print(b.name)
print(b.e_mail)
