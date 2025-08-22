def fn_if_elif_else(valor: str):
    if valor == 'a':
        print('Letra A')
    elif valor == 'b':
        print('Letra B')
    elif valor == 'c':
        print('Letra C')
    else:
        print('Valor inválido')


fn_if_elif_else('a')
fn_if_elif_else('b')
fn_if_elif_else('c')
fn_if_elif_else('d')


def fn_match_case(valor: str):
    match valor:
        case 'a':
            print('Letra A')
        case 'b':
            print('Letra B')
        case 'c':
            print('Letra C')
        case _:
            print('Valor inválido')


fn_match_case('a')
fn_match_case('b')
fn_match_case('c')
fn_match_case('d')
