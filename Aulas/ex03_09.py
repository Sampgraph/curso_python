"""
Pensando numa solução de backup de registros de autores, remova alguns registros da tabela autores abaixo
e os salve em uma lista chamada autores_backup.
A lista autores_backup deve conter os registros removidos da tabela autores.
"""


tabela_autores = [
    {'id': 1, 'nome': 'Autor 1', 'email': 'teste@teste.com', 'telefone': '1234-5678', 'biografia': 'Biografia do Autor 1'},
    {'id': 2, 'nome': 'Autor 2', 'email': 'm@m.com', 'telefone': '9876-5432', 'biografia': 'Biografia do Autor 2'},
    {'id': 3, 'nome': 'Autor 3', 'email': 'c@c.com', 'telefone': '5555-5555', 'biografia': 'Biografia do Autor 3'},
    {'id': 4, 'nome': 'Autor 4', 'email': 'd@d.com', 'telefone': '4444-4444', 'biografia': 'Biografia do Autor 4'},
]

autores_backup = []
