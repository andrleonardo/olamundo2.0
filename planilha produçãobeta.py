cucapeso1=(float(input('Qual o Peso Unitario das cuca farofa? ')))
cucapeso2=(float(input('Qual o Peso Unitario das cuca Recheada?  ')))
cucafqt=(float(input('Quantidade Cuca Farofa? ')))
cucaqt1=(float(input('Quantidade Cuca 1? ')))
cucaqt2=(float(input('Quantidade Cuca 2? ')))
scucaf= cucapeso1 * cucafqt
scuca1= cucapeso2 * cucaqt1
scuca2= cucapeso2 * cucaqt2


print('='*(30))
print('Cuca Farofa = {:.2f}Kg'.format(scucaf))
print('Cuca 1 = {:.2f}Kg'.format(scuca1))
print('Cuca 2 = {:.2f}Kg'.format(scuca2))
print('='*(30))