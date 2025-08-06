print('[Menu Principal] Escolha uma das seguintes opções:')
print('1 - Categorias')
print('2 - Editoras')
print('3 - Autores')
print('4 - Livros')
print('0 - Sair do programa')

while True:  # Loop infinito
    opcao = input('Digite a opção desejada: ')  # Entrada de dados do usuário

    if opcao == '0':
        print('Você escolheu a opção 0: Sair do programa')
        break  # Sair do loop
    elif opcao == '1':  # else if
        print('Você escolheu a opção 1: Categorias')
        input('Digite <ENTER> para continuar...')
    elif opcao == '2':
        print('Você escolheu a opção 2: Editoras')
        input('Digite <ENTER> para continuar...')
    elif opcao == '3':
        print('Você escolheu a opção 3: Autores')
        input('Digite <ENTER> para continuar...')
    elif opcao == '4':
        print('Você escolheu a opção 4: Livros')
        input('Digite <ENTER> para continuar...')
    else:
        print('Opção inválida! Tente novamente.')
        input('Digite <ENTER> para continuar...')

print('Fim do programa')

