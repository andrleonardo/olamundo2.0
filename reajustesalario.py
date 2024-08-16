salario=float(input('qual seu salario ? '))
rea=float(input('quanto de reajuste? '))
salariofinal= salario + (salario*rea/100)

print('o salario {} com {} de reajuste recebera {}'.format(salario, rea, salariofinal))