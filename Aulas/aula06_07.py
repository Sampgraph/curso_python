def saudacoes(nome):
    print(f'Olá, {nome}! Bem-vindo(a) ao Python!')


def cadastro(nome_cadastro):
    print(f'Cadastro realizado com sucesso, {nome_cadastro}!')


print('Início do programa')

n = input("Digite seu nome: ")
saudacoes(n)
cadastro(n)

print('Fim do programa')

