print('Início do programa')

def minha_funcao():  # declarando a função
    """ Função que imprime uma mensagem de saudação.
        Segunda linha do docstring.
        Terceira linha do docstring.
    """
    contador = 0
    while True:
        print(f'Olá, mundo dentro da função! {contador}')
        if contador == 5:
            print('Chegou no meio da contagem!')
            return  # Sai da função quando contador é 5

        contador += 1

    print('Saindo da função...')


print('Olá mundo fora da função!')
minha_funcao() # invocando/chamando a função

print('Fim do programa')
