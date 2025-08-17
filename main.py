menu_principal = '[Menu Principal] Escolha uma das seguintes opções: \n'\
                    '1 - Categorias \n'\
                    '2- Editoras\n' \
                    '3 - Autores \n' \
                    '4 - Livros \n' \
                    '0 - Sair do programa \n'
    ##Bloco que eu fiz a primeira impressão usando varios if (pouco produtivo)
        # print ('[Menu Principal] Escolha uma das seguintes opções:')
        # print('1 - Categorias')
        # print ('2- Editoras')
        # print('3 - Autores')
        # print('4 - Livros')
        # print('0 - Sair do programa') 

print(menu_principal) #exibe o menu que declarei Menu principal

while True:
    opcao = input('Digite a opção desejada:') #Entrada de dados do usuário

    if opcao == '0':
        print('Você escolheu a opção 0: Sair do programa')
        break #sair do menu principal        
    elif opcao == '1':
        print('Você escolheu a opção 1: SCategorias')
        input("Digite <ENTER> para continuar")
    elif opcao == '2':
        print('Você escolheu a opção 2: Editores')
        input("Digite <ENTER> para continuar")
    elif opcao == '3':
        print('Você escolheu a opção 3: Autores')
        input("Digite <ENTER> para continuar")
    elif opcao == '4':
        print('Você escolheu a opção 4: Livros')
        input("Digite <ENTER> para continuar")
    else:
        print("Opção inválida! Tente noovamente")
        input('Digite <ENTER> para continuar')
          
    
print('Fim do programa')          
dict ()