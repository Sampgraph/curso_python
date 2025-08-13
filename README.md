# Operadores matemáticos

| Operador | Operação | Exemplo |
| -------- | -------- | ------- |
| + | Adição | 2 + 3 |
| - | Subtração | 5 - 2 |
| * | Multiplicação | 10 * 4 |
| / | Divisão | 9 / 3 |


# Operadores de atribuição

| Operador | Exemplo | É o mesmo que | Comentários |
| -------- | ------- | ------------- | ----------- |
| = | x = 'Olá!' | x = 'Olá!' | Atribuição de valores |
| += | y += 10 | y = y + 10| A variável y precisa ter sido instanciada anteriormente |
| -= | z -= 20 | z = z - 20 | A variável z precisa ter sido instancianda anteriormente |

# Operadores Lógicos
| Operador | Descrição | Exemplo |
| -------- | --------- | ------- |
| and | Retorna True se todas as afirmações forem verdadeiras | `lista1 == [] and lista2 == []` |
| or  | Retorna True se uma das afirmações forem verdadeiras | `lista1 == [] or lista2 == []` |


# Tipos de dados nativos

- Inteiros (`int`)

    -2
    -1
    0
    1
    2
    3

- Números de ponto flutuante / números decimais (`float`)

    -3.14
    -0.1
    3.14
    4.5

- Booleanos (`bool`)

    True
    False

- Strings (`str`)

    'teste'
    "Olá!"
    '''Olá mundo!'''
    """Python"""

# Funções nativas em Python

- input()

    Entrada de dados.

- print()

    Saída ou exibição de dados.


# Estrutura de decisão: `if`
## if condition
```
if condition:
    expression1
```

## if-else condition
```
if condition:
    expression1
else:
    expression2
```

## if-elif-else condition
```
if condition1:
    expression1
elif condition2:
    expression2
elif condition3:
    expression3
else:
    expression4
```

# Estruturas de dados

Estruturas de Dados são uma maneira de organizar dados para que eles possam ser acessados ​​de forma mais eficiente dependendo da situação.

## Listas (`list`)

### Métodos de uma lista

| Comando | Resultado |
| ----- | ---- |
| [1, 2, 3].append(4) | [1, 2, 3, 4] |
| [1, 2, 3].clear() | [] |
| [1, 2, 3].copy() | [1, 2, 3] |
| [1, 2, 3].count(2) | 1 |
| [1, 2, 3].extend([4, 5]) | [1, 2, 3, 4, 5] |
| [1, 2, 3].index(2) | 1 |
| [1, 2, 3].insert(1, 'a') | [1, 'a', 2, 3] |
| [1, 2, 3].pop() | 3 # e a lista se torna [1, 2] |
| [1, 2, 3].pop(1) | 2 # e a lista se torna [1, 3] |
| [1, 2, 3].remove(2) | [1, 3] |
| [3, 1, 2].reverse() | [2, 1, 3] |
| [3, 1, 2].sort() | [1, 2, 3] |
| [3, 1, 2].sort(reverse=True) | [3, 2, 1] |
| [1, 2, 3] + [4, 5] | [1, 2, 3, 4, 5] |
| [1, 2, 3] * 2 | [1, 2, 3, 1, 2, 3] |
| [1, 2, 3][1:] | |
| [1, 2, 3][:2] | |
| [1, 2, 3][::-1] | |
| len([1, 2, 3]) | 3 |
