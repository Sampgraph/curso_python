def minha_funcao():  # declarando a função
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))

    print(f'O resultado da multiplicação é: {a * b}')
    if b == 0:
        print('Divisão por zero. Resultado indisponível!')
        return

    print(f'O resultado da divisão é: {a / b}')


def loop():  # declarando a função loop
    print('Início do loop')
    minha_funcao()  # invocando/chamando a função
    op = input('Deseja continuar? (s/n): ')
    if op == 'n':
        return
    else:
        loop()  # Chama a função loop recursivamente


print('Início do programa')

loop()  # Chama a função loop para iniciar o processo

print('Fim do programa')

