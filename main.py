from model.autor import Autor
from service.autor_service import AutorService
from service.categoria_service import CategoriaService
from service.editora_service import EditoraService
from service.livro_service import LivroService

from model.utils import BLUE, GREEN, RESET

menu_principal = f'''{BLUE}[Menu Principal] Escolha uma das seguintes opções:{RESET}
1 - Categorias
2 - Editoras
3 - Autores
4 - Livros
0 - Sair do programa'''



tabela_livros = []

autor_service = AutorService()
categoria_service = CategoriaService()
editora_service = EditoraService()
livro_service = LivroService()

def display_menu_principa():
    print(menu_principal)  # Exibe o menu principal
    opcao = input('[Menu Principal] Digite a opção desejada: ')  # Entrada de dados do usuário

    match opcao:
        case '0':
            print('Você escolheu a opção 0: Sair do programa')
            return  # Sair da função.
        case '1':  # else if
            categoria_service.menu()
        case '2':
            editora_service.menu()
        case '3':
            autor_service.menu()
        case '4':
            livro_service.menu()
        case _:
            print('Opção inválida! Tente novamente.')
            input('\nDigite <ENTER> para continuar...')

    display_menu_principa()  # Chama a função recursivamente para manter o menu ativo


if __name__ == '__main__':
    display_menu_principa()
    print('Fim do programa')