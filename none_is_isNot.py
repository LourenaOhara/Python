"""
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
"""

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faça algo')
else:
    print('não faça nada')

if passou_no_if is None:
    print('não passou no if')

"""OUTPUT
   *condicao = False

        não faça nada
        não passou no if

   *condicao = True

        faça algo
"""