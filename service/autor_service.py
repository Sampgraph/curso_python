from dao.autor_dao import AutorDAO
from model.autor import Autor
from model.utils import GREEN, RED, RESET


menu_autores = f'''{GREEN}[Autores] Escolha uma das seguintes opções:{RESET}
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
        match opcao_autor:
            case '0':
                return  # Sai da função e volta ao menu principal
            case '1':
                self.listar()
            case '2':
                self.cadastrar()
            case '3':
                self.excluir()
            case '4':
                self.consultar_por_id()
            case '5':
                self.editar()
            case _:
                print(f'{RED}Opção inválida! Tente novamente.{RESET}')

        input('\nDigite <ENTER> para continuar...')
        self.menu()  # Chama a função recursivamente para manter o menu ativo

    def listar(self):
        if autor_dao.read_all() == []:
            print('Não existem autores cadastrados.')
        else:
            print('ID | Nome | Email | Telefone')
            for autor in autor_dao.read_all():
                print(f"{autor}")

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
                print(f'{RED}Email inválido. Tente novamente.{RESET}')
            else:
                break  # Não ocorreu nenhuma exceção, então encerra o 'while'.

        novo_autor.email = email_autor
        autor_dao.create(novo_autor)
        print('Autor cadastrado com sucesso!')

    def excluir(self):
        if autor_dao.read_all() == []:
            print('Não existem autores cadastrados.')
        else:
            while True:
                try:
                    id_autor = int(input('Digite o ID do autor a ser excluído: '))  # cast = converte de str para int
                    autor_dao.delete(id_autor)
                except:
                    print(f'{RED}ID inválido. Tente novamente.{RESET}')
                    continue
                else:
                    break

            print('Autor excluído com sucesso!')

    def consultar_por_id(self):
        if autor_dao.read_all() == []:
            print('Não existem autores cadastrados.')
        else:
            while True:
                try:
                    id_autor = int(input('Digite o ID do autor a ser buscado: '))  # cast = converte de str para int
                    autor_encontrado = autor_dao.read(id_autor)
                except:
                    print(f'{RED}ID inválido. Tente novamente.{RESET}')
                    continue
                else:
                    break

            print('ID | Nome | Email | Telefone | Biografia')
            print(f"{autor_encontrado} | {autor_encontrado.biografia}")

    def editar(self):
        if autor_dao.read_all() == []:
            print('Não existem autores cadastrados.')
        else:
            while True:
                try:
                    id_autor = int(input('Digite o ID do autor a ser alterado: '))  # cast = converte de str para int
                    autor_editado = autor_dao.read(id_autor)
                except:
                    print(f'{RED}ID inválido. Tente novamente.{RESET}')
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
                    print(f'{RED}Email inválido. Tente novamente.{RESET}')
                else:
                    break  # Não ocorreu nenhuma exceção, então encerra o 'while'.

            autor_editado.nome = nome_autor
            autor_editado.biografia = biografia_autor
            autor_editado.telefone = telefone_autor
            autor_dao.update(id_autor, autor_editado)

            print('Autor editado com sucesso!')

