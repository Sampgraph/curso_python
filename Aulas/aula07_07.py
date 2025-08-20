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
    def __init__(self, n, t):  # Método construtor
        self.nome = n
        self.email = None
        self.telefone = t
        self.biografia = None

    def set_email(self, e):
        if is_email_valid(e):
            self.email = e
            return True
        else:
            return False



a1 = Autor('Machado de assis', '1234-5678')

email = input('Digite o email: ')
while not a1.set_email(email):
    print('Email inválido. Tente novamente.')
    email = input('Digite o email: ')

print(a1.email)

