d = {
    'chave01': {
        'subchave01': {
            'subsubchave01': {
                'nome': 'Aulas/aula04_04.py',
            }
        }
    }
}

print(d)
print(d['chave01'])
print(d['chave01']['subchave01'])
print(d['chave01']['subchave01']['subsubchave01'])
print(d['chave01']['subchave01']['subsubchave01']['nome'])

if d.get('chave01') is None:
    print('A chave "chave10" não existe no dicionário.')
else:
    print(d.get('chave01'))

print('Fim do programa')
