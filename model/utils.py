def is_email_valid(email: str) -> bool:
    if not isinstance(email, str):
        return False

    if '@' not in email or '.' not in email:
        return False

    if not email.isascii():
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

