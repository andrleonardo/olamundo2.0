# Dev LELEO
import datetime
import random
option=int(input(f'''
******************************
M E N U         P A D A R I A
[1] Calculo pão.
[2] Planilha Produção.  
[3] Calculador.
[4] Sistema Bancario
[5] Sair.

Dev Andrézin    {datetime.date.today()}
******************************
>> '''))
while option >5:
    option=int(input(f'''
******************************
M E N U         P A D A R I A
[1] Calculo pão.
[2] Planilha Produção.  
[3] Calculador.
[4] Sistema Bancario
[5] Sair.

Dev Andrézin    {datetime.date.today()}
******************************
>> '''))
if option ==1:
    print('''
*******************************
    SISTEMA CONTAGEM PÃO
*******************************
''')
    dia=datetime.date.today().weekday()
    if dia <5:
        print('''
    OK PUXEI AQUI QUE É DIA DA SEMANA
           ''')
        askpao=int(input('''
********************************                
   MANTER 110 ESTEIRAS DIARIAS?

    1 PARA SIM       2 PARA NAO                              
 ********************************                 
>>  '''))
        if askpao==1:
         paodia=110
        elif askpao==2:
         paodia=int(input('''
*********************************
Qual a quantida quer tirar hoje?
*********************************
>> '''))
        else:
         print('VALOR INCORRETO,PADRÃO MANTIDO ESTEIRAS =110.')
         paodia=110
    if dia >=5:
           print('''
OK PUXEI AQUI QUE É FINAL DE SEMANA
''')
           askpao=int(input('''
********************************                
   MANTER 140 ESTEIRAS DIARIAS?

    1 PARA SIM       2 PARA NAO                              
 ********************************                 
>> ''')) 
           if askpao==1:
              paodia=140
           elif askpao==2:
            paodia=int(input('''
*********************************
Qual a quantida quer tirar hoje?
*********************************
>> '''))
           else:
            print('VALOR INCORRETO,PADRÃO MANTIDO ESTEIRAS =140.')
            paodia=140

    adicionais=int(input('ALGUMA ESTEIRA ADICIONAL?'))
    sobrou=int(input('Quantas Esteiras Sobrou de ontem? '))

    cacetinfinal= paodia -36 -18 + adicionais - sobrou

    print(f'''
*******************************************************
            RELATORIO PARA HOJE CACETINHO!!!

[{paodia}] ESTEIRAS PARA HOJE
[{sobrou}] ESTEIRAS DE ONTEM
[36] ESTEIRAS NO GRANDÃO
[18] NA ESTUFA
[{adicionais}] ADICIONAIS
[{cacetinfinal}] VALOR PARA TIRAR!!!

Dev Andrezin! Versão: Pega careca
********************************************************
''')

if option==3:
    import math
    print('''
**************************************
          CALCULADORA DO LELEO
**************************************''')
    askcalc=int(input('''
**************************************
[1] RAIZ QUADRADA
[2] DESCONTO
[3] ADIÇÃO
[4] SUBTRAÇÃO
[5] MULTIPLICAÇÃO
[6] DIVISÃ0
[7] JUROS SIMPLES
[8] AUMENTO SALARIAL
[9] SAIR
**************************************
>> '''))
    while askcalc >9:
        askcalc=int(input('''
**************************************
[1] RAIZ QUADRADA
[2] DESCONTO
[3] ADIÇÃO
[4] SUBTRAÇÃO
[5] MULTIPLICAÇÃO
[6] DIVISÃ0
[7] JUROS SIMPLES
[8] AUMENTO SALARIAL
[9] SAIR
**************************************
>> '''))
       
    
    
    
    if askcalc==1:
     num=float(input('Qual O numero VocÊ Deseja a Raiz Quadrada? '))
     raiz= math.sqrt(num)
     print(f'A raiz quadrada de {num} e : {raiz} ')
    elif askcalc==2:
       num=float(input('Qual o valor que deseja dar o desconto? '))
       num1=float(input('Quantos Porcento de desconto? '))
       juro= num - (num * num1 /100)
       print(f'O numero {num} com {num1}% de desconto e {juro}')
    elif askcalc==3:
       num=float(input('Qual numero Deseja somar? '))
       num1=float(input(f'Somar {num} com ? '))
       resultado=num + num1
       print(f'A soma de {num} com {num1} = {resultado}')
    elif askcalc==4:
       num=float(input('Qual Numero deseja Subtrair? '))
       num1=float(input(f'Subtrair {num} com? '))
       resultado=num - num1
       print(f'Subtrair {num} com {num1} = {resultado}')
    elif askcalc==5:
       num=float(input('Qual Numero deseja multiplicar? '))
       num1=float(input(f'Multiplicar {num} com? '))
       resultado=num * num1
       print(f'{num} multiplicado por {num1} = {resultado}')
    elif askcalc==6:
       num=float(input('Qual numero deseja dividir? '))
       num1=float(input(f'Dividir {num} por ?'))
       resultado=num /num1
       print(f'{num} divido por {num1} = {resultado}')
    elif askcalc==7:
       num=float(input('Qual Numero deseja acrescentar juros? '))
       num1=float(input('Quantos porcento de juros?'))
       resultado= num + (num * num1 /100)
       print(f'{num} com {num1}% = {resultado}')
    elif askcalc==8:
       num=float(input('Qual o Salario '))
       num1=float(input('Quantos porcento de reajuste?? '))
       resultado= num + (num * num1 /100)
       print(f'{num} com {num1}% = {resultado}')
    elif askcalc==9:
       print('Adios!')
elif option==4:
   saldo=300
   limiteconta=250
   limitesaque=3
   transfdiar=0
   bolso=30
   dia=datetime.date.today()
   while True:
      askbanco=int(input(f'''
*******************************
        BANCO DO LELEO
SALDO={saldo} LIMITE CONTA={limiteconta}
                         
[1] EXTRATO
[2] SACAR
[3] TRANSFERIR
[4] DEPOSITAR
[5] SAIR

{dia} Dev LeLEo                        
*********************************                         
'''))
    
      if askbanco==1:
         print(f'''
*********************************
        E X T R A T O
[{saldo}] Saldo Atual.
[{limiteconta}] Limite conta.
[{transfdiar}] Transferencias Realizadas Hoje.
[{limitesaque}] Limite Saques diario.
''')
      if askbanco==2:
         sacar=float(input('''
*********************************
        S A Q U E J A 
*********************************                 
VALOR PARA SAQUE >>  '''))
         if limitesaque ==0:
            print('Limite Saque Excedido')
         else:
            if sacar > saldo:
              print('Pobre do caralho')
            elif sacar < saldo:
              print(f'Ok,Realizando o saque de {sacar}!!')
              saldo= saldo - sacar
              bolso=+ sacar
              limitesaque= limitesaque -1
              transfdiar= transfdiar +1
              print(f'Valor de conta é {saldo}')
             
      
      elif askbanco==3:
         print('Não Habilidatado ainda')
      elif askbanco==4:
         depositar=float(input('''
*********************************
        D E P O S I T E   J A 
*********************************                 
VALOR PARA DEPOSITO >>  '''))
         
         if bolso < depositar:
               askbolso=int(input(f'''
****************************************************
SENTIMOS MUITO MAS O VALOR ESTÁ ABAIXO DO DEPOSITADO 
            
        Valor inserido={depositar}
        Valor Disponivel={bolso}

        PROCESSAR O VALOR DISPINIVEL?
    1 SIM                   2 NAO
*****************************************************                                   
>> '''))
               if askbolso ==1:
                  saldo= saldo + bolso
                  bolso= bolso - bolso
                  print('Ok valor depositado')
               else:
                 print('Ok Até Logo')
         if bolso >= depositar:
            bolso= bolso - depositar
            saldo= saldo + depositar
            print('Ok valor depositado')

    





elif option ==5:
    print('Tchau seu corno!')
