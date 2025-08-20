class Autor:
    def __init__(self, n, e, t):  # Método construtor
        self.nome = n
        self.email = e
        self.telefone = t
        self.biografia = None

a = Autor('Machado de assis', 'machado@teste.com', '1234-5678')
a.biografia = 'N/A'
print(a.nome)
print(a.email)
print(a.telefone)
print(a.biografia)


b = Autor('Cecília', 'meireles@teste.com', '9876-5432')
b.biografia = 'Biografia da Cecília'

print(b.nome)
print(b.email)
print(b.telefone)
print(b.biografia)