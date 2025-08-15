def formata_data(dia, mes, ano='2025'):
    return f'{dia:02d}/{mes:02d}/{ano}'


print('Inicio do programa!')


data = formata_data(14, 8, 2030)  # passando o valor já atrelando ao nome do parâmetro.
print(data)


data = formata_data(14, 8)  # passando o valor já atrelando ao nome do parâmetro.
print(data)

print('Fim do programa!')
