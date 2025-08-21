def is_odd(inteiro: int) -> bool:
    if inteiro % 2 == 0:
        return False # número par
    else:
        return True # número ímpar


def is_odd_desaconselhavel(inteiro: int) -> bool:  # Apesar da anotação de tipo avisar que o retorno é do tipo 'bool', a função pode retornar qualquer outro tipo.
    if inteiro % 2 == 0:
        return 'Falso' # número par
    else:
        return 'Verdadeiro' # número ímpar


print(is_odd(1))
print(is_odd(2))


print(is_odd_desaconselhavel(1))
print(is_odd_desaconselhavel(2))


