def soma(a, b):
    print(f'O resultado da soma é: {a + b}')


print('Início do programa')

soma(5, 10)  # Chama a função soma com os argumentos 5 e 10

soma(20, 30)  # Chama a função soma com os argumentos 20 e 30

soma(100, 200)  # Chama a função soma com os argumentos 100 e 200

soma(-50, 23 )  # Chama a função soma com os argumentos -50 e 23

soma('Olá, ', 'Python!')  # Chama a função soma com strings


try:
    soma()
except TypeError as e:
    print(f'Erro: {e}')

try:
    soma(3)
except TypeError as e:
    print(f'Erro: {e}')


def multiplicacao(a, b, c):
    print(f'O resultado da multiplicação é: {a * b * c}')


multiplicacao(2, 3, 4)  # Chama a função multiplicacao com os argumentos 2, 3 e 4

multiplicacao(1, 5, 10)  # Chama a função multiplicacao com os argumentos 1, 5 e 10

multiplicacao(0, 0, 0)  # Chama a função multiplicacao com os argumentos 0, 0 e 0

try:
    multiplicacao()
except TypeError as e:
    print(f'Erro: {e}')

try:
    multiplicacao(2)
except TypeError as e:
    print(f'Erro: {e}')

try:
    multiplicacao(2, 3)
except TypeError as e:
    print(f'Erro: {e}')



print('Fim do programa')
