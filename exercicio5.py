"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    if(numero_int % 2 == 0):
        print(f'O número {numero_int} é par')
    else:
        print(f'O número {numero_int} é impar')
else:
    print(f'O número {numero} não é inteiro')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horas = input('Poderia me informar que horas são(hh:mm)? ')
horas_fat = horas[0:2]

if horas_fat >= '0' and horas_fat <= '11':
    print('Bom dia')
elif horas_fat >= '12' and horas_fat <= '17':
    print('Boa tarde')
else:
    print('Boa noite')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
if len(nome) < 5:
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) < 7:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')