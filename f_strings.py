#IMC
#f-strings
nome = 'Lourena Ohara'
altura = 1.67
peso = 71
imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'


print('PRINT COM F-STRINGS')
print('\n')
print(linha_1)
print(linha_2)
print(linha_3)

"""OUTPUT
    PRINT COM F-STRINGS


    Lourena Ohara tem 1.67 de altura
    pesa 71 quilos e seu imc é
    25.46
"""