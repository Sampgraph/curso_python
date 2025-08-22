def square(x):
    return x ** 2


print(f'O quadrado de 2 é: {square(2)}')
print(f'O quadrado de 3 é: {square(3)}')
print(f'O quadrado de 4 é: {square(4)}')


square_lambda = lambda x: x ** 2

print(f'O quadrado de 2 é: {square_lambda(2)}')
print(f'O quadrado de 3 é: {square_lambda(3)}')
print(f'O quadrado de 4 é: {square_lambda(4)}')