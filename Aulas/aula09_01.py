class Imovel:
    # Atributos de classe
    numero_de_quartos = 3
    numero_de_salas = 2
    numero_de_banheiros = 2

    def __init__(self):
        # Atributos de instância
        self.cor = None
        self.piso = None


apto01 = Imovel()
apto01.cor = 'Azul'
apto01.piso = 'Marmore'
Imovel.numero_de_quartos = 4
Imovel.numero_de_salas = 3
Imovel.numero_de_banheiros = 3

print(apto01.cor)
print(apto01.piso)
print(apto01.numero_de_quartos)
print(apto01.numero_de_salas)
print(apto01.numero_de_banheiros)

print('*' * 80)

apto02 = Imovel()
apto02.cor = 'Vermelho'
apto02.piso = 'Pedra'

print(apto02.cor)
print(apto02.piso)
print(apto02.numero_de_quartos)
print(apto02.numero_de_salas)
print(apto02.numero_de_banheiros)

print('*' * 80)
