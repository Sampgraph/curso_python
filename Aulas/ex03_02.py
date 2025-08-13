# Tendo um CPF dentro de uma string no formato '12345678900',
# desenvolva um programa para imprimir esse CPF no formato: '123.456.789-00'

# 1ª solução

s1 = ''
cpf = '123456789XY'

for index in range(0, 3):
    s1 += cpf[index]  # é o mesmo que s1 = s1 + cpf[index]

s2 = ''
for index in range(3,6):
    s2 += cpf[index]

s3 = ''
for index in range(6,9):
    s3 += cpf[index]

vefiricador = ''
for index in range(9,11):
    vefiricador += cpf[index]


print(f'{s1}.{s2}.{s3}-{vefiricador}')

# 2ª solução
s1 = cpf[0:3]
s2 = cpf[3:6]
s3 = cpf[6:9]
vefiricador = cpf[9:11]

print(f'{s1}.{s2}.{s3}-{vefiricador}')
