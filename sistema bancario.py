import datetime
mes=datetime.date.today()
diain=datetime.date.today().weekday()
if diain==0:
  dia='Segunda-Feira'
elif diain==1:
  dia='Terça-Feira'
elif diain==2:
  dia='Quarta-Feira'
elif diain==3:
    dia='Quinta-Feira'
elif diain==4:
    dia='Sexta-Feira'
elif diain==5:
    dia='Sabado'
elif diain==6:
    dia='Domingo'
else:
    dia='Bug'
dictlogin= {'044.666.555.56': {'nome': 'André Leonardo De Lima matana','senha':'leleo'}           } 




def cadastrarcheck():
    print('''
***********************************
        Ficamos Muito Feliz 
    em saber que quer participar
***********************************''')
    askcpf=str(input('Qual seu CPF? [Sem ponto e espaço] ')).strip()
    resultado= askcpf in dictlogin
    if resultado==True:
       print('Já Existe seu CPF no nosso sitema!!')
    else:
       if len(askcpf)==11:
         print('A implementar')
       
       
       
       else:
          print('CPF INVALIDO')

menuoptionlogin=6
while menuoptionlogin >4:
     menuoptionlogin=(int(input(f'''
*********************************************************
*           * M E N U    B A N C O   L E L E O*         *
*{dia} - {mes}        ************                      *
*********************************************************                                                          
*[1] Se Cadastrar             [3]  Creditos:            *
*[2] Fazer Login              [4]  Sair:                *
*********************************************************
>> ''')))
     if menuoptionlogin==1:
            cadastrarcheck()
     elif menuoptionlogin==2:
       print('A Implementar')
     elif menuoptionlogin==3:
       print('A Implementar')
     elif menuoptionlogin==4:
       print('Até Mais!!')
       break
     else:
       print('Bug')
