# input: funciona em strings de forma a gerar concatenação
# ou reptição de letras e palavras

nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
print(f'A soma dos números é: {numero_1 + numero_2}')

"""OUTPUT
    Qual o seu nome? Lourena
    O seu nome é Lourena
    Digite um número: 1
    Digite outro número: 2
    A soma dos números é: 12
"""

#typecasting com verificação de tipo da variável
numero_3 = input('Digite um número: ')
numero_4 = input('Digite outro número: ')

int_numero_3 = int(numero_3)
int_numero_4 = int(numero_4)

print(f'A soma dos números é: {int_numero_3 + int_numero_4}')

"""OUTPUT
    Digite um número: 3
    Digite outro número: 4
    A soma dos números é: 7
"""