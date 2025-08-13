# slicing ou fatiamento
# é uma forma de acessar partes de uma string, lista ou tupla
# utilizando a notação [início:fim:passo]
# onde 'início' é o índice do primeiro elemento a ser incluído,
# 'fim' é o índice do primeiro elemento a ser excluído,
# e 'passo' é o intervalo entre os índices (opcional, padrão é 1).


cpf = '123456789ZY'

print(f'{cpf[0:9]}')

print(f'{cpf[0:11:2]}') # números ímpares
print(f'{cpf[1:11:2]}') # números pares

# inverter a string
print(f'A string inversa é: {cpf[::-1]}')  # inverte a string