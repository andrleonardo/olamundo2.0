import datetime
mes=datetime.date.today()
pegadia=datetime.date.today().weekday()
diassemana=['Segunda Feira','Terça Feira','Quarta Feira','Quinta Feira','Sexta Feira','Sabado','Domingo']
dia=diassemana[pegadia]



print(f'''  
******************************************      
{mes} ---------------------{dia}
          BEM Vindos A LOJA DO 
      ANDRÉ LEONARDO DE LIMA MATANA 
******************************************
 ''')

valorDoPedido=float(input('Valor Do Pedido? '))
quantidadeParcela=float(input('Quantas Parcelas? '))

if quantidadeParcela <4:
    juros=0
elif quantidadeParcela <6:
    juros=4
elif quantidadeParcela <9:
    juros=8
elif quantidadeParcela <13:
    juros=16
else:
    juros=32

ValorDaParcelaSemJuros= valorDoPedido / quantidadeParcela 
ValorTotalDaParcela= (valorDoPedido/ quantidadeParcela) + (ValorDaParcelaSemJuros * juros /100)
ValorTotalParcelado= ValorTotalDaParcela * quantidadeParcela

print(f'''
******************************''')
