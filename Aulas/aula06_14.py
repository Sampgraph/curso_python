def formata_data(**kwargs):
    dia = kwargs.get('dia')
    mes = kwargs.get('mes')
    ano = kwargs.get('ano', '2025')
    return f'{dia:02d}/{mes:02d}/{ano}'



print('Inicio do programa!')


data = formata_data(ano=2030, mes=8, dia=14)  # passando o valor já atrelando ao nome do parâmetro.
print(data)


data = formata_data(mes=8, dia=14)  # passando o valor já atrelando ao nome do parâmetro.
print(data)

print('Fim do programa!')
