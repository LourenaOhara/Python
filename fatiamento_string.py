"""
Fatiamento de strings
012345678910111213
Im your father
-1413121110987654321
Fatiamento [i:f:p] [::]
Obs.: a funçãi len retorna a qtd
de caracteres de str
"""

variavel = 'Im your father'
print(variavel[3])
print(variavel[-10])
print(variavel[4:11])
print(variavel[4:])
print(variavel[:11])
print(variavel[-13:-3])
print(len(variavel))
#fatiamento = i-> inicio -> fim p-> pulo
print(variavel[0:14:1])
print(variavel[0:14:3])
print(variavel[0:14:5])
print(variavel[::-1]) #string ao contrario
print(variavel[-1:-15:-1]) #string ao contrario

"""OUTPUT
    o
    our fat
    our father
    Im your fat
    m your fat
    14
    Im your father
    Iyrae
    Iut
    rehtaf ruoy mI
    rehtaf ruoy mI
"""