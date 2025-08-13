livro = {
    'titulo': 'Python para desenvolvedores',
    'ano': 2023,
    'paginas': 500,
    'isbn': '978-85-551-0000-0',
    'resumo': 'Aprenda Python do básico ao avançado com exemplos práticos.',
    'autor': {
        'nome': 'Machado',
        'email': 'm@m.com',
        'telefone': '987',
        'biografia': 'Fusce molestie urna quis egestas fermentum. Cras eget lobortis nisl. Suspendisse feugiat enim nec augue sollicitudin faucibus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Quisque sapien tortor, dignissim in sapien eget, posuere commodo urna. Proin eget posuere tortor, aliquam porta massa. Donec molestie ornare libero pretium semper. Sed congue ligula id ex dapibus eleifend. Fusce malesuada justo ac ligula dictum scelerisque.'
    },
    'categoria': {
        'nome': 'Romance'
    },
    'editora': {
        'nome': 'Cia das Letras',
        'endereco': 'Rua Um 1',
        'telefone': '123'
    }
}

print(f"{livro['titulo']} | {livro['ano']} | {livro['paginas']} | {livro['isbn']} | {livro['autor']['nome']} | {livro['categoria']['nome']} | {livro['editora']['nome']}")
