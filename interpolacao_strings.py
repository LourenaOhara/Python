"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal
"""

nome = 'Lourena'
preco = 72633.7334
variavel = '%s, o preço e R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))

"""OUTPUT
    Lourena, o preço e R$72633.73
    O hexadecimal de 1500 é 000005DC
"""