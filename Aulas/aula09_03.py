def media(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4

resultado = media(2.4, 5.6, 9.8, 7)
print(f'A média do ano é: {resultado}')



media_l = lambda x1, x2, x3, x4: (x1 + x2 + x3 + x4) / 4

resultado_l = media_l(2.4, 5.6, 9.8, 7)
print(f'A média do ano é: {resultado_l}')
