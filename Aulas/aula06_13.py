def formata_data(dia, mes, ano):
    return f'{dia:02d}/{mes:02d}/{ano}'


print('Inicio do programa!')


data = formata_data(ano=2025, mes=8, dia=14)  # passando o valor já atrelando ao nome do parâmetro.
print(data)


data = formata_data(ano=25, mes=8, dia=14)  # passando o valor já atrelando ao nome do parâmetro.
print(data)

print('Fim do programa!')
