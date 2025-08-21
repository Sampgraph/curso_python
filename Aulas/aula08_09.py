from aula08_08 import Aluno

# class Aluno:
#     def __init__(self, nome: str, sobrenome: str):
#         self.nome = nome
#         self.sobrenome = sobrenome

#     def __str__(self):
#         return f'Nome: {self.nome} Sobrenome: {self.sobrenome}'

print('Início do programa')

print('Cadastro de Alunos!')

a = Aluno('João', 'Martins')
print(a)

print('Fim do programa')

print(f'Nome do módulo: {__name__}')
