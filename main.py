from model.autor import Autor
from service.autor_service import AutorService
from model.utils import BLUE, GREEN, RESET

menu_principal = f'''{BLUE}[Menu Principal] Escolha uma das seguintes opções:{RESET}
1 - Categorias
2 - Editoras
3 - Autores
4 - Livros
0 - Sair do programa'''

menu_categorias = f'''{GREEN}[Categorias] Escolha uma das seguintes opções:{RESET}
1 - Listar toda as categorias
2 - Adicionar nova categoria
3 - Excluir categoria
4 - Ver categoria por Id
0 - Voltar ao menu anterior'''

menu_editoras = f'''{GREEN}[Editoras] Escolha uma das seguintes opções:{RESET}
1 - Listar todas as editoras
2 - Adicionar nova editora
3 - Excluir editora
4 - Ver editora por Id
0 - Voltar ao menu anterior'''

menu_livros = f'''{GREEN}[Livros] Escolha uma das seguintes opções:{RESET}
1 - Listar todos os livros
2 - Adicionar novo livro
3 - Excluir livro
4 - Ver livro por Id
5 - Editar livro
0 - Voltar ao menu anterior'''


tabela_categorias = []
tabela_editoras = []
tabela_livros = []

autor_service = AutorService()


def bloco_categoria() -> None:
    """

    Bloco da CATEGORIA

    """
    print(menu_categorias)
    opcao_categoria = input('Digite a opção: ')
    if opcao_categoria == '0':
        return  # Sai da função e volta ao menu principal
    elif opcao_categoria == '1':
        if tabela_categorias == []:
            print('Não existem categorias cadastradas.')
        else:
            print('ID | Nome')
            for index, categoria in enumerate(tabela_categorias):
                print(f"{index + 1} | {categoria['nome']}")
    elif opcao_categoria == '2':
        nome_categoria = input('Digite o nome da categoria: ')
        nova_categoria = {
            'nome': nome_categoria
        }
        tabela_categorias.append(nova_categoria)
        print('Categoria cadastrada com sucesso!')
    elif opcao_categoria == '3':
        if tabela_categorias == []:
            print('Não existem categorias cadastradas.')
        else:
            while True:
                try:
                    id_categoria = int(input('Digite o ID da categoria a ser excluída: '))
                    tabela_categorias.pop(id_categoria - 1)
                except:
                    print('ID inválido. Tente novamente.')
                    continue
                else:
                    break

            print('Categoria excluída com sucesso!')
    elif opcao_categoria == '4':
        if tabela_categorias == []:
            print('Não existem categorias cadastradas.')
        else:
            while True:
                try:
                    id_categoria = int(input('Digite o ID do categoria a ser consultada: '))
                    categoria = tabela_categorias[id_categoria - 1]
                except:
                    print('ID inválido. Tente novamente.')
                    continue
                else:
                    break

            print('ID | Nome')
            print(f"{id_categoria} | {categoria['nome']}")
    elif opcao_categoria == '5':
        if tabela_categorias == []:
            print('Não existem categorias cadastradas.')
        else:
            while True:
                try:
                    id_categoria = int(input('Digite o ID da categoria a ser editada: '))
                    categoria = tabela_categorias[id_categoria - 1]
                except:
                    print('ID inválido. Tente novamente.')
                    continue
                else:
                    break

            nome_categoria = input('Digite o nome da categoria: ')
            categoria['nome'] = nome_categoria
            print('Categoria editada com sucesso!')
    else:
        print('Opção inválida!')

    input('\nDigite <ENTER> para continuar...\n')
    bloco_categoria()  # Chama a função recursivamente para manter o menu ativo


def bloco_editora() -> None:
    """

    Bloco da EDITORA

    """
    print(menu_editoras)
    opcao_editora = input('Digite a opção: ')
    if opcao_editora == '0':
        return  # Sai da função e volta ao menu principal
    elif opcao_editora == '1':
        if tabela_editoras == []:
            print('Não existem editoras cadastradas.')
        else:
            print('ID | Nome | Endereço | Telefone')
            for index, editora in enumerate(tabela_editoras):
                print(f"{index + 1} | {editora['nome']} | {editora['endereco']} | {editora['telefone']}")
    elif opcao_editora == '2':
        nome_editora = input('Digite o nome da editora: ')
        endereco_editora = input('Digite o endereço da editora: ')
        telefone_editora = input('Digite o telefone da editora: ')
        nova_editora = {
            'nome': nome_editora,
            'endereco': endereco_editora,
            'telefone': telefone_editora
        }
        tabela_editoras.append(nova_editora)
        print('Editora cadastrada com sucesso!')
    elif opcao_editora == '3':
        if tabela_editoras == []:
            print('Não existem editoras cadastradas.')
        else:
            while True:
                try:
                    id_editora = int(input('Digite o ID da editora a ser excluída: '))
                    tabela_editoras.pop(id_editora - 1)
                except:
                    print('ID inválido. Tente novamente.')
                    continue
                else:
                    break
            print('Editora excluída com sucesso!')
    elif opcao_editora == '4':
        if tabela_editoras == []:
            print('Não existem editoras cadastradas.')
        else:
            while True:
                try:
                    id_editora = int(input('Digite o ID da editora a ser consultada: '))
                    editora = tabela_editoras[id_editora - 1]
                except:
                    print('ID inválido. Tente novamente.')
                    continue
                else:
                    break

            print('ID | Nome | Endereço | Telefone')
            print(f"{id_editora} | {editora['nome']} | {editora['endereco']} | {editora['telefone']}")
    elif opcao_editora == '5':
        if tabela_editoras == []:
            print('Não existem editoras cadastradas.')
        else:
            while True:
                try:
                    id_editora = int(input('Digite o ID da editora a ser editada: '))
                    editora = tabela_editoras[id_editora - 1]
                except:
                    print('ID inválido. Tente novamente.')
                    continue
                else:
                    break

            nome_editora = input('Digite o nome da editora: ')
            endereco_editora = input('Digite o endereço da editora: ')
            telefone_editora = input('Digite o telefone da editora: ')

            editora['nome'] = nome_editora
            editora['endereco'] = endereco_editora
            editora['telefone'] = telefone_editora

            print('Editora editada com sucesso!')
    else:
        print('Opção inválida!')

    input('\nDigite <ENTER> para continuar...\n')
    bloco_editora()  # Chama a função recursivamente para manter o menu ativo


def bloco_livro() -> None:
    """

    Bloco do LIVRO

    """
    print(menu_livros)
    opcao_livro = input('Digite a opção: ')
    if opcao_livro == '0':
        return  # Sai da função e volta ao menu principal
    elif opcao_livro == '1':
        if tabela_livros == []:
            print('Não existem livros cadastrados.')
        else:
            print('ID | Título | Ano | Páginas | ISBN | Autor | Categoria | Editora')
            for index, livro in enumerate(tabela_livros):
                print(f"{index + 1} | {livro['titulo']} | {livro['ano']} | {livro['paginas']} | {livro['isbn']} | {livro['autor']['nome']} | {livro['categoria']['nome']} | {livro['editora']['nome']}")
    elif opcao_livro == '2':
        if tabela_autores == [] or tabela_editoras == [] or tabela_categorias == []:
            print('É necessário ter pelo menos um autor, uma editora e uma categoria cadastrados para adicionar um livro.')
        else:
            titulo = input('Digite o título do livro: ')
            ano = input('Digite o ano de publicação do livro: ')
            paginas = input('Digite o número de páginas do livro: ')
            isbn = input('Digite o ISBN do livro: ')
            resumo = input('Digite o resumo do livro: ')
            while True:
                try:
                    id_autor = int(input('Digite o ID do autor do livro: '))
                    autor_tabela = tabela_autores[id_autor - 1]
                except:
                    print('ID inválido. Tente novamente.')
                    continue
                else:
                    break

            while True:
                try:
                    id_categoria = int(input('Digite o ID da categoria do livro: '))
                    categoria_tabela = tabela_categorias[id_categoria - 1]
                except:
                    print('ID inválido. Tente novamente.')
                    continue
                else:
                    break
            while True:
                try:
                    id_editora = int(input('Digite o ID da editora do livro: '))
                    editora_tabela = tabela_editoras[id_editora - 1]
                except:
                    print('ID inválido. Tente novamente.')
                    continue
                else:
                    break

            novo_livro = {
                'titulo': titulo,
                'ano': ano,
                'paginas': paginas,
                'isbn': isbn,
                'resumo': resumo,
                'autor': autor_tabela,
                'categoria': categoria_tabela,
                'editora': editora_tabela
            }
            tabela_livros.append(novo_livro)
            print('Livro cadastrado com sucesso!')
    elif opcao_livro == '3':
        if tabela_livros == []:
            print('Não existem livros cadastrados.')
        else:
            while True:
                try:
                    id_livro = int(input('Digite o ID do livro a ser excluído: '))
                    tabela_livros.pop(id_livro - 1)
                except:
                    print('ID inválido. Tente novamente.')
                    continue
                else:
                    break

            print('Livro excluído com sucesso!')
    elif opcao_livro == '4':
        if tabela_livros == []:
            print('Não existem livros cadastrados.')
        else:
            while True:
                try:
                    id_livro = int(input('Digite o ID do livro a ser consultado: '))
                    livro = tabela_livros[id_livro - 1]
                except:
                    print('ID inválido. Tente novamente.')
                    continue
                else:
                    break

            print('ID | Título | Ano | Páginas | ISBN | Autor | Categoria | Editora | Resumo')
            print(f"{id_livro} | {livro['titulo']} | {livro['ano']} | {livro['paginas']} | {livro['isbn']} | {livro['autor']['nome']} | {livro['categoria']['nome']} | {livro['editora']['nome']} | {livro['resumo']}")
    elif opcao_livro == '5':
        if tabela_livros == []:
            print('Não existem livros cadastrados.')
        else:
            while True:
                try:
                    id_livro = int(input('Digite o ID do livro a ser editado: '))
                    livro = tabela_livros[id_livro - 1]
                except:
                    print('ID inválido. Tente novamente.')
                    continue
                else:
                    break

            titulo_livro = input('Digite o título do livro: ')
            print('Livro editado com sucesso!')
    else:
        print('Opção inválida! Tente novamente.')

    input('\nDigite <ENTER> para continuar...')
    bloco_livro()  # Chama a função recursivamente para manter o menu ativo


while True:  # Loop infinito
    print(menu_principal)  # Exibe o menu principal
    opcao = input('[Menu Principal] Digite a opção desejada: ')  # Entrada de dados do usuário

    if opcao == '0':
        print('Você escolheu a opção 0: Sair do programa')
        break  # Sair do loop
    elif opcao == '1':  # else if
        bloco_categoria()
    elif opcao == '2':
        bloco_editora()
    elif opcao == '3':
        autor_service.menu()
    elif opcao == '4':
        bloco_livro()
    else:
        print('Opção inválida! Tente novamente.')
        input('\nDigite <ENTER> para continuar...')

print('Fim do programa')

