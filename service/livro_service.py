from dao.autor_dao import AutorDAO
from dao.categoria_dao import CategoriaDAO
from dao.editora_dao import EditoraDAO
from dao.livro_dao import LivroDAO
from model.livro import Livro
from model.utils import GREEN, RED, RESET


menu_livros = f'''{GREEN}[Livros] Escolha uma das seguintes opções:{RESET}
1 - Listar todos os livros
2 - Adicionar novo livro
3 - Excluir livro
4 - Ver livro por Id
5 - Editar livro
0 - Voltar ao menu anterior'''

autor_dao = AutorDAO()
categoria_dao = CategoriaDAO()
editora_dao = EditoraDAO()
livro_dao = LivroDAO()


class LivroService:

    def menu(self):
        print(menu_livros)
        opcao_livro = input('Digite a opção: ')
        match opcao_livro:
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
        if livro_dao.is_empty():
            print('Não existem livros cadastrados.')
            return

        print('ID | Título | Ano | Páginas | ISBN | Autor | Categoria | Editora')
        for livro in livro_dao.read_all():
            print(f"{livro}")

    def cadastrar(self):
        if autor_dao.is_empty() or categoria_dao.is_empty() or editora_dao.is_empty():
            print('É necessário ter pelo menos um autor, uma editora e uma categoria cadastrados para adicionar um livro.')
            return

        titulo = input('Digite o título do livro: ')
        ano = input('Digite o ano de publicação do livro: ')
        paginas = input('Digite o número de páginas do livro: ')
        isbn = input('Digite o ISBN do livro: ')
        resumo = input('Digite o resumo do livro: ')
        novo_livro = Livro(titulo, ano, paginas, isbn, resumo)

        while True:
            try:
                id_autor = int(input('Digite o ID do autor do livro: '))
                autor = autor_dao.read(id_autor)
            except:
                print('ID inválido. Tente novamente.')
                continue
            else:
                novo_livro.autor = autor
                break

        while True:
            try:
                id_categoria = int(input('Digite o ID da categoria do livro: '))
                categoria = categoria_dao.read(id_categoria)
            except:
                print('ID inválido. Tente novamente.')
                continue
            else:
                novo_livro.categoria = categoria
                break

        while True:
            try:
                id_editora = int(input('Digite o ID da editora do livro: '))
                editora = editora_dao.read(id_editora)
            except:
                print('ID inválido. Tente novamente.')
                continue
            else:
                novo_livro.editora = editora
                break

        livro_dao.create(novo_livro)
        print('Livro cadastrado com sucesso!')

    def excluir(self):
        if livro_dao.is_empty():
            print('Não existem livros cadastrados.')
            return

        while True:
            try:
                id_livro = int(input('Digite o ID do livro a ser excluído: '))  # cast = converte de str para int
                livro_dao.delete(id_livro)
            except:
                print(f'{RED}ID inválido. Tente novamente.{RESET}')
                continue
            else:
                break

        print('Livro excluído com sucesso!')

    def consultar_por_id(self):
        if livro_dao.is_empty():
            print('Não existem livros cadastrados.')
            return

        while True:
            try:
                id_livro = int(input('Digite o ID do livro a ser buscado: '))  # cast = converte de str para int
                livro_encontrado = livro_dao.read(id_livro)
            except:
                print(f'{RED}ID inválido. Tente novamente.{RESET}')
                continue
            else:
                break

        print('ID | Título | Ano | Páginas | ISBN | Autor | Categoria | Editora | Resumo')
        print(f"{livro_encontrado} | {livro_encontrado.resumo}")


    def editar(self):
        if livro_dao.is_empty():
            print('Não existem livros cadastrados.')
            return

        if autor_dao.is_empty() or categoria_dao.is_empty() or editora_dao.is_empty():
            print('É necessário ter pelo menos um autor, uma editora e uma categoria cadastrados para editar um livro.')
            return


        while True:
            try:
                id_livro = int(input('Digite o ID do livro a ser editado: '))
                livro_editado = livro_dao.read(id_livro)
            except:
                print(f'{RED}ID inválido. Tente novamente.{RESET}')
                continue
            else:
                break

        titulo = input('Digite o título do livro: ')
        ano = input('Digite o ano de publicação do livro: ')
        paginas = input('Digite o número de páginas do livro: ')
        isbn = input('Digite o ISBN do livro: ')
        resumo = input('Digite o resumo do livro: ')
        livro_editado.titulo = titulo
        livro_editado.ano = ano
        livro_editado.paginas = paginas
        livro_editado.isbn = isbn
        livro_editado.resumo = resumo

        while True:
            try:
                id_autor = int(input('Digite o ID do autor do livro: '))
                autor = autor_dao.read(id_autor)
            except:
                print('ID inválido. Tente novamente.')
                continue
            else:
                livro_editado.autor = autor
                break

        while True:
            try:
                id_categoria = int(input('Digite o ID da categoria do livro: '))
                categoria = categoria_dao.read(id_categoria)
            except:
                print('ID inválido. Tente novamente.')
                continue
            else:
                livro_editado.categoria = categoria
                break

        while True:
            try:
                id_editora = int(input('Digite o ID da editora do livro: '))
                editora = editora_dao.read(id_editora)
            except:
                print('ID inválido. Tente novamente.')
                continue
            else:
                livro_editado.editora = editora
                break

        livro_dao.update(id_livro, livro_editado)
        print('Livro editado com sucesso!')

