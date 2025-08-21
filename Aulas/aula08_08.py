class Aluno:
    def __init__(self, nome: str, sobrenome: str):
        self.nome = nome
        self.sobrenome = sobrenome

    def __str__(self):
        return f'Nome: {self.nome} Sobrenome: {self.sobrenome}'


if __name__ == '__main__':
    aluno = Aluno('Maria', 'Silva')
    print(aluno)

