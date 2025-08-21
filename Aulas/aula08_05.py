def saudacoes(nome: str):  # Anotações de tipo ou Typing Annotations
    print(type(nome))
    print(f'Olá, {nome}! Bem-vindo(a) ao Python!')


def cadastro(nome: str): # Anotações de tipo ou Typing Annotations
    print(type(nome))
    print(f'Cadastro realizado com sucesso, {nome}!')


print('Início do programa')

nome = input("Digite seu ID: ")
saudacoes(nome)
cadastro(nome)

print('Fim do programa')
