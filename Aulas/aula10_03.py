class Aluno:
    __tabela_alunos = []  # Atributo de classe representando a tabela de alunos.

    def __init__(self, n: str):
        Aluno.__tabela_alunos.append(n)
        self.nome = n

    @classmethod  # Decorator
    def get_tabela_alunos(cls):
        return Aluno.__tabela_alunos


aluno1 = Aluno('Maria')
print(aluno1.nome)
print('Conteúdo da tabela:', Aluno.get_tabela_alunos())
print('ID da tabela', id(Aluno.get_tabela_alunos()))

aluno2 = Aluno('João')
print(aluno2.nome)
print('Conteúdo da tabela:', Aluno.get_tabela_alunos())
print('ID da tabela', id(Aluno.get_tabela_alunos()))

aluno3 = Aluno('José')
print(aluno3.nome)
print('Conteúdo da tabela:', Aluno.get_tabela_alunos())
print('ID da tabela', id(Aluno.get_tabela_alunos()))

