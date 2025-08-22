def pos_neg(x):
    if x > 0:
        return 'Positivo'
    elif x < 0:
        return 'Negativo'
    else:
        return 'Zero'


print(f'O número é {pos_neg(5)}')
print(f'O número é {pos_neg(-5)}')
print(f'O número é {pos_neg(0)}')


pos_neg_lambda = lambda x: 'Positivo' if x > 0 else 'Negativo' if x < 0 else 'Zero'

print(f'O número é {pos_neg_lambda(5)}')
print(f'O número é {pos_neg_lambda(-5)}')
print(f'O número é {pos_neg_lambda(0)}')
