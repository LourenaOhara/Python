"""
    Formatação básica de strings
    s - string
    d - int
    f - float
    .<número de dígitos>f
    x ou X - Hexadecimal
    (Caractere)(><^)(quantidade)
    > - Esquerda
    < - Direita
    ^ - Centro
    Sinal - + ou -
    Ex.: 0>-100, .1f
    Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{100.73436565254:-.1f}')
print(f'{100.73436565254:+.1f}')
print(f'{100.73436565254:0>+10.1f}')
print(f'{100.73436565254:0>+10,.1f}')
print(f'{100.73436565254:0=+10.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'O hexadecimal de 1500 é {1500:08X}')

"""OUTPUT
    ABC
            ABC
    ABC       .
        ABC    .
    100.7
    +100.7
    0000+100.7
    0000+100.7
    +0000100.7
    O hexadecimal de 1500 é 000005dc
    O hexadecimal de 1500 é 000005DC
"""