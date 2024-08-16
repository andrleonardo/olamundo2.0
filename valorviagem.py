distancia=float(input('Qual a distancia? '))
if distancia <= 200:
    valord=0.45
else:
    valord=0.50
soma= distancia * valord
print('A distancia é {}Km o valor promocional ficou {:.2f} o valor total ficou {:.2f}'.format(distancia,valord,soma))