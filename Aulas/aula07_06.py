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


class Autor:
    def __init__(self, n, e, t):  # Método construtor
        self.nome = n
        if is_email_valid(e):
            self.email = e
        else:
            self.email = None  # Ainda não resolvemos o nosso problema.

        self.telefone = t
        self.biografia = None



a1 = Autor('Machado de assis', 'machado@teste.com', '1234-5678')
print(a1.email)
a2 = Autor('Cecília', 'meireles_teste.com', '9876-5432')
print(a2.email)

