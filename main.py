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
                print('ID | Nome | Email | Telefone')
                for index, autor in enumerate(tabela_autores, start=1):
                    print(f"{index} | {autor['nome']} | {autor['email']} | {autor['telefone']}")
            elif opcao_autor == '2':
                print('Adicionando novo autor...')
                nome_autor = input('Digite o nome do autor: ')
                email_autor = input('Digite o email do autor: ')
                biografia_autor = input('Digite a biografia do autor: ')
                telefone_autor = input('Digite o telefone do autor: ')
                novo_autor = {
                    'nome': nome_autor,
                    'email': email_autor,
                    'telefone': telefone_autor,
                    'biografia': biografia_autor
                }
                tabela_autores.append(novo_autor)
                print('Autor cadastrado com sucesso!')
            elif opcao_autor == '3':
                print('Excluindo autor...')
                id_autor = int(input('Digite o ID do autor a ser excluído: '))  # cast = converte de str para int
                tabela_autores.pop(id_autor - 1)  # -1 para ajustar o índice
                print('Autor excluído com sucesso!')
            elif opcao_autor == '4':
                print('Buscando autor por Id...')
                id_autor = int(input('Digite o ID do autor a ser buscado: '))  # cast = converte de str para int
                autor_encontrado = tabela_autores[id_autor - 1]
                print('ID | Nome | Email | Telefone | Biografia')
                print(f"{id_autor} | {autor_encontrado['nome']} | {autor_encontrado['email']}  | {autor_encontrado['telefone']} | {autor_encontrado['biografia']}")
            elif opcao_autor == '5':
                print('Editando autor...')
                id_autor = int(input('Digite o ID do autor a ser buscado: '))  # cast = converte de str para int
                autor_editado = tabela_autores[id_autor - 1]
                nome_autor = input('Digite o nome do autor: ')
                email_autor = input('Digite o email do autor: ')
                biografia_autor = input('Digite a biografia do autor: ')
                telefone_autor = input('Digite o telefone do autor: ')
                autor_editado['nome'] = nome_autor
                autor_editado['email'] = email_autor
                autor_editado['telefone'] = telefone_autor
                autor_editado['biografia'] = biografia_autor
                print('Autor editado com sucesso!')
            else:
                print('Opção inválida! Tente novamente.')

            input('Digite <ENTER> para continuar...')
    elif opcao == '4':
        print(menu_livros)
    else:
        print('Opção inválida! Tente novamente.')

    input('Digite <ENTER> para continuar...')

print('Fim do programa')

