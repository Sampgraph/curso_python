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
    def __init__(self, t):  # Método construtor
        self.__nome = None
        self.__email = None  # Convenção para definir um atributo como 'protegido'.
        self.telefone = t
        self.biografia = None

    @property  # Decorator ou decoradores
    def nome(self):
        return self.__nome

    @nome.setter  # Decorator ou decoradores
    def nome(self, n):
        self.__nome = n.title()

    @property  # Decorator ou decoradores
    def email(self):
        return self.__email

    @email.setter  # Decorator ou decoradores
    def email(self, e):
        if is_email_valid(e):
            self.__email = e.lower()
            return
        else:
            raise ValueError('Email inválido')




a1 = Autor('1234-5678')
a1.nome = 'machado de assis'

e = input('Digite o email: ')

while True:
    try:
        a1.email = e
        break  # Encerra o 'while'
    except:
        print('Email inválido. Tente novamente.')
        e = input('Digite o email: ')
        continue


print(a1.nome)
print(a1.email)
