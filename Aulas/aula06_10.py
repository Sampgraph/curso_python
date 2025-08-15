def valida_email(email):
    if not isinstance(email, str):
        return False

    if '@' not in email or '.' not in email:
        return False

    return True


print('Início do programa')

resultado = valida_email(1000) # Teste com um número

if resultado:  # se VERDADEIRO
    print('Email válido')
else:
    print('Email inválido')


resultado = valida_email('teste') # Teste com um número

if resultado:  # se VERDADEIRO
    print('Email válido')
else:
    print('Email inválido')


resultado = valida_email('a@teste.com') # Teste com um número

if resultado: # se VERDADEIRO
    print('Email válido')
else:
    print('Email inválido')

print('Fim do programa')

