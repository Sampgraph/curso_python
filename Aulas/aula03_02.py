lista = ['Python', [1, 2, 3], True, 45.67, 'Fiap']
print(lista)  # Exibe a lista original

print(lista[1])  # Acessa o segundo elemento da lista, que é uma lista

lista_interna = lista[1]  # Acessa a lista interna

lista_interna[0] = 'a'
lista_interna[1] = 'b'
lista_interna[2] = 'c'
lista_interna.append('d')  # Adiciona um novo elemento à lista interna

print(lista_interna)  # Exi

printi('teste')

print(lista)  # Exibe a lista original, que agora contém a lista modificada


