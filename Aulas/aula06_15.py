def formata_data1(dia, mes):
    return f'{dia:02d}/{mes:02d}/2025'

def formata_data2(dia, mes, ano):
    return f'{dia:02d}/{mes:02d}/{ano}'


print('Inicio do programa!')


data = formata_data2(ano=2026, mes=8, dia=14)  # passando o valor já atrelando ao nome do parâmetro.
print(data)


data = formata_data1(mes=8, dia=14)  # passando o valor já atrelando ao nome do parâmetro.
print(data)

print('Fim do programa!')
