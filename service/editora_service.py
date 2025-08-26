from dao.editora_dao import EditoraDAO
from model.editora import Editora
from model.utils import GREEN, RED, RESET


menu_editoras = f"""
{GREEN}[Editoras] Escolha uma das seguintes opções:{RESET}
1 - Listar todas as editoras
2 - Adicionar nova editora
3 - Excluir editora
4 - Ver editora por Id
5 - Editar editora
0 - Voltar ao menu anterior
"""


class EditoraService:
    editora_dao: EditoraDAO = EditoraDAO()

    def menu(self):
        print(menu_editoras)
        escolha = input('Digite a opção: ')

        match escolha:
            case '0':
                return
            case '1':
                self.listar()
            case '2':
                self.adicionar()
            case '3':
                self.remover()
            case '4':
                self.consultar_por_id()
            case '5':
                self.editar()
            case _:
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

    def consultar_por_id(self):
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

    def editar(self):
        if EditoraService.editora_dao.is_empty():
            print("Nenhuma Editora cadastrada.")
            return

        while True:
            try:
                id_editora = int(input('Digite o ID da editora a ser alterada: '))  # cast =
                editora = EditoraService.editora_dao.read(id_editora)
            except:
                print(f'{RED}ID inválido. Tente novamente.{RESET}')
                continue
            else:
                break

        nome = input('Digite o nome da editora: ')
        endereco = input('Digite o endereço da editora: ')
        telefone = input('Digite o telefone da editora: ')
        editora.nome = nome
        editora.endereco = endereco
        editora.telefone = telefone
        EditoraService.editora_dao.update(id_editora, editora)

        print('Editora editada com sucesso!')