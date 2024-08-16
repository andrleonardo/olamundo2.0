#cuca farofa
qtcucaf=int(input('Quantidade Cuca Farofa? '))
if qtcucaf ==0:
    print('Ok sem cuca farofa!!')
else:
    print('Peso padrão das Cuca Farofa?')
    cucaf=int(input('======= 1=SIM ===== 2=NÃO ======? '))
    if cucaf<=1:
        valorf=qtcucaf*0.498
    else:
         ask=float(input('Qual O Peso unitario da cuca Farofa?'))
         valorf=qtcucaf*ask

#pão doce
qtpaod=int(input('Quantidade pão doce?'))
if qtpaod >0:
   print('Valor Padrão da Forma inteira de pão doce?')
   valorpd=int(input('======= 1=SIM ==== 2=NÃO?====='))
   if valorpd <=1:
       valor=qtpaod*4.387 
   else:
        paodoce=float(input('Qual o peso pão doce?'))
        valor= paodoce *qtpaod
else:
    print('Ok sem pão doce.')
#cuca recheada
qtcucar=int(input('Quantidade cuca Recheada? '))
if qtcucar ==0:
    print('Ok Sem Cuca recheada!')
elif qtcucar <=10:
    sabor1=str(input('Sabor um? '))
elif qtcucar <=20:
    sabor1=str(input('Sabor um ?'))
    sabor2=str(input('Sabor dois? '))
elif qtcucar <=30:
    sabor1=str(input('Sabor um? '))
    sabor2=str(input('Sabor dois? '))
    sabor3=str(input('Sabor Três? '))
elif qtcucar <=40:
    sabor1=str(input('Sabor um? '))
    sabor2=str(input('Sabor Dois? '))
    sabor3=str(input('Sabor três? '))
    sabor4=str(input('Sabor Quatro? '))
elif qtcucar <=50:
    sabor1=str(input('Sabor Um? '))
    sabor2=str(input('Sabor Dois?'))
    sabor3=str(input('Sabor Três'))
    sabor4=str(input('Sabor quatro? '))
    sabor5=str(input('Sabor cinco? '))
else:
    print('vai toma no teu cu')

print('Saiu Creme?')
saiul=float(input('======= 1=SIM ==== 2=NÂO========? '))
if saiul <=1:
    leits=int(input('Quantos leite? '))
    valol=leits + (leits*0.800)
    
else:
    print('Ok sem Creme!')

#relatorio
print('='*15,'Relátorio','='*15)

if qtcucaf >0:
    print('Cuca Farofa: {:.2f}Kg'.format(valorf))
else:
    print('-')
if qtpaod >0:
    print('Pão Doce:    {:.2f}Kg'.format(valor))
else:
    print('-')
if saiul <=1:
    print('Creme:       {}L'.format(valol))
else:
    print('-')

print('='*18,'Fim','='*18)