from dao.autor_dao import AutorDAO
from model.autor import Autor


menu_autores = '''[Autores] Escolha uma das seguintes opções:
1 - Listar todos os autores
2 - Adicionar novo autor
3 - Excluir autor
4 - Ver autor por Id
5 - Editar autor
0 - Voltar ao menu anterior'''


autor_dao = AutorDAO()


class AutorService:

    def menu(self):
        print(menu_autores)
        opcao_autor = input('[Autores] Digite a opção desejada: ')
        if opcao_autor == '0':
            return  # Sai da função e volta ao menu principal
        elif opcao_autor == '1':
            self.listar()
        elif opcao_autor == '2':
            self.cadastrar()
        elif opcao_autor == '3':
            self.excluir()
        elif opcao_autor == '4':
            self.consultar_por_id()
        elif opcao_autor == '5':
            self.editar()
        else:
            print('Opção inválida! Tente novamente.')

        input('\nDigite <ENTER> para continuar...')
        self.menu()  # Chama a função recursivamente para manter o menu ativo

    def listar(self):
        if autor_dao.tabela_autores == []:
            print('Não existem autores cadastrados.')
        else:
            print('ID | Nome | Email | Telefone')
            for index, autor in enumerate(autor_dao.tabela_autores, start=1):
                print(f"{index} | {autor} ")

    def cadastrar(self):
        nome_autor = input('Digite o nome do autor: ')
        biografia_autor = input('Digite a biografia do autor: ')
        telefone_autor = input('Digite o telefone do autor: ')
        novo_autor = Autor(nome_autor, telefone_autor, biografia_autor)
        while True:
            try:
                email_autor = input('Digite o email do autor: ')
                novo_autor.email = email_autor
            except:
                print('Email inválido. Tente novamente.')
            else:
                break  # Não ocorreu nenhuma exceção, então encerra o 'while'.

        novo_autor.email = email_autor
        autor_dao.tabela_autores.append(novo_autor)
        print('Autor cadastrado com sucesso!')

    def excluir(self):
        if autor_dao.tabela_autores == []:
            print('Não existem autores cadastrados.')
        else:
            while True:
                try:
                    id_autor = int(input('Digite o ID do autor a ser excluído: '))  # cast = converte de str para int
                    autor_dao.tabela_autores.pop(id_autor - 1)  # -1 para ajustar o índice
                except:
                    print('ID inválido. Tente novamente.')
                    continue
                else:
                    break

            print('Autor excluído com sucesso!')

    def consultar_por_id(self):
        if autor_dao.tabela_autores == []:
            print('Não existem autores cadastrados.')
        else:
            while True:
                try:
                    id_autor = int(input('Digite o ID do autor a ser buscado: '))  # cast = converte de str para int
                    autor_encontrado = autor_dao.tabela_autores[id_autor - 1]
                except:
                    print('ID inválido. Tente novamente.')
                    continue
                else:
                    break

            print('ID | Nome | Email | Telefone | Biografia')
            print(f"{id_autor} | {autor_encontrado} | {autor_encontrado.biografia}")

    def editar(self):
        if autor_dao.tabela_autores == []:
            print('Não existem autores cadastrados.')
        else:
            while True:
                try:
                    id_autor = int(input('Digite o ID do autor a ser buscado: '))  # cast = converte de str para int
                    autor_editado = autor_dao.tabela_autores[id_autor - 1]
                except:
                    print('ID inválido. Tente novamente.')
                    continue
                else:
                    break

            nome_autor = input('Digite o nome do autor: ')
            biografia_autor = input('Digite a biografia do autor: ')
            telefone_autor = input('Digite o telefone do autor: ')
            while True:
                try:
                    email_autor = input('Digite o email do autor: ')
                    autor_editado.email = email_autor
                except:
                    print('Email inválido. Tente novamente.')
                else:
                    break  # Não ocorreu nenhuma exceção, então encerra o 'while'.

            autor_editado.nome = nome_autor
            autor_editado.telefone = telefone_autor
            autor_editado.biografia = biografia_autor
            print('Autor editado com sucesso!')

