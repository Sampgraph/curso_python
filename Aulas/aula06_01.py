def minha_funcao():  # declarando a função
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))

    print(f'O resultado da multiplicação é: {a * b}')
    if b == 0:
        print('Divisão por zero. Resultado indisponível!')
        return

    print(f'O resultado da divisão é: {a / b}')


print('Início do programa')

op = ''

while op != 'n':
    minha_funcao()  # invocando/chamando a função
    op = input('Deseja continuar? (s/n): ')

print('Fim do programa')

