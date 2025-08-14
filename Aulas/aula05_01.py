lista  = ['Machado', 'Cecília', 'Saramago', 'Tolkien', 'João Cabral']

novo_autor = input('Digite o nome do novo autor: ')
lista.append(novo_autor)

while True:
    id_autor_str = input('Digite o ID do autor a ser excluído: ')
    if id_autor_str.isdigit():
        id_autor = int(id_autor_str)
    else:
        print('ID inválido. Tente novamente.')
        continue

    if id_autor < 1 or id_autor > len(lista):
        print('ID inválido. Tente novamente.')
    else:
        break

lista.pop(id_autor - 1)

print(lista)

print('Fim do programa')
