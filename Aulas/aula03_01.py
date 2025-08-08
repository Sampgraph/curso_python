lista = ['Python', 123, True, 45.67, 'Fiap']

for index, valor in enumerate(lista, start=100):
    print(index, valor)



lista.pop(1)

print(lista)
