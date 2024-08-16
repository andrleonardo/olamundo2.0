valorc=0
valorcr=0
pesol=0
valorcs=0
valorcdl=0

option=int(input('''Oque Deseja? 
[1] Calculo pão cacetinho 
[2] Planilha produção 
[3] Calculadora
[4] Sair
# '''))
while option  >5:
    option=int(input('Option Incorreta, Oque Deseja? [1] Calculo pão cacetinho \n [2] Planilha produção?    '))
if option==4:
    print('Até a próxima!') 
if option==3:
    num1=float(input('Primeiro Número? '))
    num2=float(input('''
Segundo Número? 
caso não Coloque 
[0]
$   '''))
    print('='*30)
    optionmat=int(input('''Deseja
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
[5] Raiz Quadrada
[6] Sair:
$  '''))
    while optionmat >=7:
        optionmat=int(input('''Opção incorreta Digite:
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
[5] Raiz Quadrada
[6] Sair:
 $  '''))
    if optionmat==1:
        soma=num1 + num2
        print('A Soma de {} + {} Ficou = {}'.format(num1,num2,soma))
    if optionmat==2:
        soma=num1 - num2
        print('A Subtração de {} + {} Ficou = {}'.format(num1,num2,soma))
    if optionmat==3:
        soma=num1 * num2
        print('A Multiplicação de {} + {} Ficou = {}'.format(num1,num2,soma))
    if optionmat==4:
        soma=num1 / num2
        print('A Divisão de {} + {} Ficou = {}'.format(num1,num2,soma))
    if optionmat==5:
        import math
        soma= math.sqrt(num1)
        print('A Raiz quadrada de {} Ficou = {}'.format(num1,soma))
    if optionmat==6:
        print('Até Logo!')
if option==1:
    qtpaodia=int(input('Quantos Pão Para Hoje? '))
    qtpaoontem=int(input('Quantos Pão Sobrou? '))
    qtpaoest=int(input('Quantos Pão Naquela estufa? '))
    qtpao1=int(input('Acrecentar mais esteiras para tirar? '))
    qtpao2=int(input('Descontar Algumas Esteiras? '))
    sobraas=int(input('Quantas Assadas sobrou? '))
    somapao= qtpaodia - qtpaoontem - qtpaoest + qtpao1 - qtpao2 -36
    print('='*20)
    print('''Relatório Cacetinho:
[{}] Pão Para O DIA
[{}] Sobra De Ontem
[{}] Pão Assado
[{}] Restantes para tirar
[ 1] Estufa Grande!'''.format(qtpaodia,qtpaoontem,sobraas,somapao))
    print('='*20)
if option==2:
    print('Vamos anexar os dados a Planilha então!')
    cucaf=int(input('Qual Quantidade Cuca Farofa? '))
    cucar=int(input('Qual Quantidade Cuca Recheada? '))
    paodoce=int(input('Quantas Formas Pão Doce?'))
    quantoslitsl=int(input('Quantos Litros De Leite Creme? '))
    sonhobau=int(input('Quantos Sonhos Baunilha? '))
    sonhodl=int(input('Quantos Sonhos Doce De Leite? '))
    if cucaf >=1:
        print('O Peso Unitario da cuca Farofa é [0.498g] ou Alterar?')
        altr=str(input('S/N ? ')).strip() .upper()
        while altr not in 'SN':
            altr=str(input('S/N ? ')).strip() .upper()
        if altr=='S':
            valorsc=float(input('Qual O Peso Unitario das cuca Farofa? '))
            print('O novo Peso Unitario da cuca Farofa é [{}]g'.format(valorsc))
            valorc=valorsc *cucaf
        if altr=='N':
            valorc=0.498 * cucaf
            print('O Peso Unitario da cuca Farofa é [0.498g]')
            print('='*20)
    if cucar >=1:
        print('O peso Padrão unitario da cuca recheado é [0.408g] ou alterar?')
        askcuca=str(input('S/N')).strip() .upper()
        while askcuca not in'SN':
            input('S/N?').strip() .upper()
        if askcuca == 'S':
            receba=float(input('Qual o novo peso unitario das cuca recheada? '))
            valorrr= receba * cucar
        if askcuca == 'N':
            receba= 0.408
            valorrr=receba * cucar
           
    print(f'Ok O peso das cucas recheadas em unidade é igual a {receba}g')
    print('='*20)
    print('Ok agora vamos adicionar quantidade de sabores!!')
    askquantiasabor=int(input('Quantos sabores de cuca quer adicionar??'))

    
    
    
    if paodoce >=1:
         print('O Peso da forma pão doce é [4.387Kg] ou Alterar?')
         altrrp=str(input('S/N ? ')).strip() .upper()
         while altrrp not in 'SN':
            altrrp=str(input('S/N ? ')).strip() .upper()
         if altrrp=='S':
            valorcrtt=float(input('Qual O Peso da forma de pão doce? '))
            valorcr=paodoce * valorcrtt
            print('O novo Peso da forma pão doce é [{}Kg]'.format(valorcrtt))
         if altrrp=='N':
            valorcr=4.387 * paodoce
            print('O Peso da forma de pão doce é [4.387kg]')
            print('='*20)
    if quantoslitsl >=1:
         pacotes=int(input('Quantos Pacotes de creme? '))
         pesol= quantoslitsl + (pacotes * 0.778)
         print('='*20)
    if sonhobau >=1:
        print('O Peso Unitario Do Sonho Baunilha é [0.179g] ou Alterar?')
        altrb=str(input('S/N ? ')).strip() .upper()
        while altrb not in 'SN':
            altrb=str(input('S/N ? ')).strip() .upper()
        if altrb=='S':
            valorcst=float(input('Qual O Peso Unitario Do Sonho Baunilha? '))
            valorcs= valorcst * sonhobau
            print('O novo Peso Unitario do Sonho Baunilha é [{}]g'.format(valorcst))
        if altrb=='N':
            valorcs=0.179 * sonhobau
            print('O Peso Unitario do Sonho Baunilha é [0.179g]')
            print('='*20)
    if sonhodl>=1:
        print('O Peso Unitario Do Sonho Doce De Leite é [0.179g] ou Alterar?')
        altrdl=str(input('S/N ? ')).strip() .upper()
        while altrdl not in 'SN':
            altrdl=str(input('S/N ? ')).strip() .upper()
        if altrdl=='S':
            valorcdll=float(input('Qual O Peso Unitario Sonho Doce De Leite? '))
            print('O novo Peso Unitario do Sonho doce de lete é [{}]g'.format(valorcdll))
            valorcdl= valorcdll *sonhodl
        if altrdl=='N':
            valorcdl=0.498 * cucaf
            print('O Peso Unitario da cuca Farofa é [0.498g]')
            print('='*20)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print('''
Cuca Farofa:       [{}Kg]
Creme Confeiteiro: [{} L]
Pão Doce           [{}Kg]
Sonho Baunilha     [{}Kg]
Sonho Doce De Leite[{}Kg]

'''.format(valorc,pesol,valorcr,valorcs,valorcdl))
         







    