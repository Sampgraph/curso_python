lista  = ['Machado', 'Cecília', 'Saramago', 'Tolkien', 'João Cabral']

novo_autor = input('Digite o nome do novo autor: ')
lista.append(novo_autor)

while True:
    try:
        id_autor_str = input('Digite o ID do autor a ser excluído: ')
        id_autor = int(id_autor_str)
        lista.pop(id_autor - 1)
        # print(10/0)  # Simula um erro para testar o tratamento de exceção
    except ValueError:
        print(f'ID inválido: {id_autor_str}. Tente novamente.')
        continue
    except IndexError:
        print(f'ID inválido: {id_autor}. Tente novamente.')
        continue
    except Exception as e:
        print(f'Ocorreu um erro: {e}. Tente novamente.')
    else:  # Se não houver exceções, sai do loop
        break


print(lista)
print('Fim do programa')
