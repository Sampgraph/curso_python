def is_email_valid(email):
    if not isinstance(email, str):
        return False

    if '@' not in email or '.' not in email:
        return False

    partes = email.split('@')  # desmembrando a string
    if len(partes) != 2:
        return False

    username = partes[0]
    dominio = partes[1]

    if not username or not dominio:
        return False

    if '.' not in dominio:
        return False

    if dominio.startswith('.') or dominio.endswith('.'):
        return False

    if ' ' in username or ' ' in dominio:
        return False

    return True


print('Início do programa')

print(is_email_valid('empresa.com.br'))
print(is_email_valid(1000))
print(is_email_valid('well@email@empresa.com.br'))
print(is_email_valid('empresa.com.br@teste'))
print(is_email_valid('a@teste.com'))

print('Fim do programa!')