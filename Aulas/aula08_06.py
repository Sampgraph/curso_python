def minha_funcao(a: str, b: int, c: float, d: bool, e: list):
    if not isinstance(a, str):
        raise TypeError('O parâmetro a deve ser uma string')

    if not isinstance(b, int):
        raise TypeError('O parâmetro b deve ser um inteiro')

    if not isinstance(c, float):
        raise TypeError('O parâmetro c deve ser um float')

    if not isinstance(d, bool):
        raise TypeError('O parâmetro d deve ser um booleano')

    if not isinstance(e, list):
        raise TypeError('O parâmetro e deve ser uma lista')

    # Depois das validações, faço uso das variáveis/parâmetros que chegaram.
    print('Fim da função')


minha_funcao('1', 2, 3.14, True, ['a', 'b', 'c'])


