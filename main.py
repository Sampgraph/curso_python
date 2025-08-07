menu_principal = '''[Menu Principal] Escolha uma das seguintes opções:
1 - Categorias
2 - Editoras
3 - Autores
4 - Livros
0 - Sair do programa'''

menu_categorias = '''[Categorias] Escolha uma das seguintes opções:
1 - Listar toda as categorias
2 - Adicionar nova categoria
3 - Excluir categoria
4 - Ver categoria por Id
0 - Voltar ao menu anterior'''

menu_editoras = '''[Editoras] Escolha uma das seguintes opções:
1 - Listar todas as editoras
2 - Adicionar nova editora
3 - Excluir editora
4 - Ver editora por Id
0 - Voltar ao menu anterior'''

menu_autores = '''[Autores] Escolha uma das seguintes opções:
1 - Listar todos os autores
2 - Adicionar novo autor
3 - Excluir autor
4 - Ver autor por Id
5 - Editar autor
0 - Voltar ao menu anterior'''

menu_livros = '''[Livros] Escolha uma das seguintes opções:
1 - Listar todos os livros
2 - Adicionar novo livro
3 - Excluir livro
4 - Ver livro por Id
5 - Editar livro
0 - Voltar ao menu anterior'''

tabela_autores = [] # list()

while True:  # Loop infinito
    print(menu_principal)  # Exibe o menu principal
    opcao = input('[Menu Principal] Digite a opção desejada: ')  # Entrada de dados do usuário

    if opcao == '0':
        print('Você escolheu a opção 0: Sair do programa')
        break  # Sair do loop
    elif opcao == '1':  # else if
        print(menu_categorias)
    elif opcao == '2':
        print(menu_editoras)
    elif opcao == '3':
        while True:
            print(menu_autores)
            opcao_autor = input('[Autores] Digite a opção desejada: ')
            if opcao_autor == '0':
                print('Voltando ao menu principal...')
                break  # Sair do loop interno
            if opcao_autor == '1':
                print('Listando todos os autores...')
                print('Nome | Email | Telefone | Biografia')
                for autor in tabela_autores:
                    print(autor[0], '|', autor[1], '|', autor[2], '|', autor[3])
            elif opcao_autor == '2':
                print('Adicionando novo autor...')
                nome_autor = input('Digite o nome do autor: ')
                email_autor = input('Digite o email do autor: ')
                biografia_autor = input('Digite a biografia do autor: ')
                telefone_autor = input('Digite o telefone do autor: ')
                novo_autor = []
                novo_autor.append(nome_autor)
                novo_autor.append(email_autor)
                novo_autor.append(telefone_autor)
                novo_autor.append(biografia_autor)
                tabela_autores.append(novo_autor)
                print('Autor cadastrado com sucesso!')
            elif opcao_autor == '3':
                print('Excluindo autor...')
            elif opcao_autor == '4':
                print('Buscando autor por Id...')
            elif opcao_autor == '5':
                print('Editando autor...')
            else:
                print('Opção inválida! Tente novamente.')

            input('Digite <ENTER> para continuar...')
    elif opcao == '4':
        print(menu_livros)
    else:
        print('Opção inválida! Tente novamente.')

    input('Digite <ENTER> para continuar...')

print('Fim do programa')

