def is_email_valid(email: str) -> bool:  # Função 'is_email_valid' simplificada para efeito didático.
    if not isinstance(email, str):
        return False

    if '@' not in email or '.' not in email:
        return False

    if not email.isascii():
        return False

    return True


e = 'x@y.com'
f = 'joão@t.com'

print(f'O email {e} é válido? {is_email_valid(e)}')
print(f'O email {f} é válido? {is_email_valid(f)}')


is_email_valid_lambda = lambda email: True if isinstance(email, str) and '@' in email and '.' in email and email.isascii() else False

print(f'O email {e} é válido? {is_email_valid_lambda(e)}')
print(f'O email {f} é válido? {is_email_valid_lambda(f)}')