from dao.editora_dao import EditoraDAO
from model.editora import Editora


menu_editoras = """
{GREEN}[Editoras] Escolha uma das seguintes opções:{RESET}
1 - Listar todas as editoras
2 - Adicionar nova editora
3 - Excluir editora
4 - Ver editora por Id
0 - Voltar ao menu anterior
"""


class EditoraService:
    editora_dao: EditoraDAO = EditoraDAO()

    def menu(self):
        print(menu_editoras)
        escolha = input('Digite a opção: ')

        if escolha == '0':
            return
        elif escolha == '1':
            self.listar()
        elif escolha == '2':
            self.adicionar()
        elif escolha == '3':
            self.remover()
        elif escolha == '4':
            self.mostrar_por_id()
        else:
            print('Opção inválida. Por favor, tente novamente!')

        input('\nDigite <ENTER> para continuar...')
        self.menu()

    def listar(self):
        try:
            editoras = EditoraService.editora_dao.read_all()
            if editoras:
                for editora in editoras:
                    print('Id | Nome | Endereço | Telefone')
                    print(editora)
            else:
                print('Nenhuma editora encontrada!')


        except Exception as e:
            print(f'Erro ao exibir as editoras! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def adicionar(self):
        print('\nAdicionando editora...')

        nome = input('Digite o nome da editora: ')
        endereco = input('Digite o endereço da editora: ')
        telefone = input('Digite o telefone da editora: ')
        nova_editora = Editora(nome, endereco, telefone)
        try:
            EditoraService.editora_dao.create(nova_editora)
        except Exception as e:
            print(f'Erro ao inserir editora! - {e}')
        else:
            print('Editora adicionada com sucesso!')

        input('Pressione uma tecla para continuar...')

    def remover(self):
        if EditoraService.editora_dao.is_empty():
            print("Nenhuma Editora cadastrada.")
            return

        print('\nRemovendo editora...')

        try:
            editora_id = int(input('Digite o ID da excluir para excluir: '))
            if (EditoraService.editora_dao.delete(editora_id)):
                print('Editora excluída com sucesso!')
            else:
                print('Editora não encontrada!')
        except Exception as e:
            print(f'Erro ao excluir editora! - {e}')
            return

    def mostrar_por_id(self):
        if EditoraService.editora_dao.is_empty():
            print("Nenhuma Editora cadastrada.")
        else:
            print('\nEditora por Id...')

            try:
                id = int(input('Digite o Id da editora para buscar: '))
                edt = EditoraService.editora_dao.read(id)
                if edt:
                    print('Id | Nome | Endereço | Telefone')
                    print(edt)
                else:
                    print('Editora não encontrada!')
            except Exception as e:
                print(f'Erro ao exibir editora! - {e}')
                return
