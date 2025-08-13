tabela_usuarios = []

user1 = {
    'email': 'well@w.com',
    'password': '123456',
    'website': 'https://www.fiap.com.br',
}

tabela_usuarios.append(user1)

user2 = {
    'email': 'teste@t.com',
    'password': 'abcdef',
}

tabela_usuarios.append(user2)

for user in tabela_usuarios:
    print(f'{user["email"]} | {user["password"]} | {user.get("website", "N/A")}')

print('Fim do programa')