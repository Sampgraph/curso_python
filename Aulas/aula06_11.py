def soma2(a, b):
    print(f'O resultado da soma é: {a + b}')

def soma3(a, b, c):
    print(f'O resultado da soma é: {a + b + c}')

def soma4(a, b, c, d):
    print(f'O resultado da soma é: {a + b + c + d}')


def soma(*args):
    resultado = 0
    for elemento in args:
        resultado += elemento

    print(f'O resultado da soma é: {resultado}')


print('Início do programa')

soma2(5, 10)  # Chama a função soma com os argumentos 5 e 10
soma3(5, 10, 15)  # Chama a função soma3 com os argumentos 5, 10 e 15
soma4(5, 10, 15, 20)  # Chama a função soma4 com os argumentos 5, 10, 15 e 20

print('*' * 80)

soma()
soma(10)
soma(5, 10)
soma(5, 10, 15)
soma(5, 10, 15, 20)
soma(1, 2, 3, 4, 5, 6, 7, 10, 20, 30, 40, 50, 100)

print('Fim do programa')