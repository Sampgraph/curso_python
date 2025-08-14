def minha_funcao():
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))

    print(f'O resultado da soma é: {a + b}')


minha_funcao()  # invocando/chamando a função da linha #1

backup_minha_funcao = minha_funcao  # Backup da função original

"""
Várias linhas de código!!!
Várias linhas de código!!!
Várias linhas de código!!!
Várias linhas de código!!!

"""

def minha_funcao():  # A boa prática sugere evitar repetir nome de função
    nome = input("Digite seu nome: ")
    print(f'Olá, {nome}! Bem-vindo(a) à função!')


minha_funcao()  # invocando/chamando a função da linha #18
backup_minha_funcao()  # Chama a função de backup para manter o comportamento original