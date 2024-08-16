import datetime
pegadia=datetime.date.today().weekday() # sapoha pega de 0 a 6 equivalente o dia da semana sendo 0 segunda e 6 domigno
diassemana=['Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira','Sexta-Feira','Sábado','Domingo'] # lista dias semanas
import  mysql.connector
#conexão mysql
conexao = mysql.connector.connect(
host='',
user='',
password='',
database='',
)
cursor=conexao.cursor()



def menupadaria():
    menuoption=5
    while menuoption >4:
        menuoption=int(input((f'''
********************************************
##################{diassemana[pegadia]}##############
[1] Calculo Pão Cacetinho.
[2] Planilha Produção.
[3] Sair.
[4] Consultar Cacetinhos
*****************************************************
>> ''')))
        if menuoption==1:
            if pegadia <=4:
                askquantiacacete=int(input('''
********************************
Dia De Semana são 110 Esteiras

    1 = Manter      2 = Alterar          
*********************************
>> '''))
                if askquantiacacete ==1:
                    catedia=110
                else:
                    try:
                     catedia=int(input('Qual A Quantia de esteiras hoje ?? '))
                    except ValueError:
                        print('Valor Valido por favor')    
                        
            
                        

            else:
                askquantiacacete=int(input('''
********************************
Dia Final de Semana são 140 Esteiras

    1 = Manter      2 = Alterar          
*********************************
>> '''))
                if askquantiacacete ==1:
                    catedia=140
                else:
                    try:
                        catedia=int(input('Qual A Quantia de esteiras hoje ?? '))
                    except ValueError:
                        print('Valor Valido por favor')
            askcrua=int(input('Quantas Massas Crescidas Crua sobrou? '))
            askassada=int(input('Quantas Massas Assadas Sobrou? '))
            try:
                askestufa=int(input('A Quantia Na Estufa Se Mantem 18? 1 = SIM 2 = NÃO  '))
            except ValueError:
                print('VALOR ENTRE 1 E 2')
            if askestufa ==1:
                paoestufa=18
            else:
                try:
                 paoestufa=int(input('Quantas Na estufa? '))
                    
                except ValueError:
                 print('Valor Correto Por favor')
            try:       
                askgrande=int(input('Quantia no grandão = 36 SE MANTEM? 1 = SIM  2 = NÃO  '))
            except ValueError:
                print('Valor Entre 1 e 2')
            if askgrande==1:
                paogrande=36
            else:
                try:
                    paogrande=int(input('Qual A Quantia vai ser colocado no grandão? '))
                except ValueError:
                    print('Valor Correto Por favor')
            askadicional=int(input('Qual A Quantia de esteiras Adicionais? '))
            soma=(catedia -askcrua - paoestufa - paogrande) + askadicional

            print(f'''
***********************************
        Relatorio Cacetinho
[{catedia}] Esteiras Para O DIA
[{askcrua}] Esteiras Sobra Crua
[{askassada}] Esteiras Sobra Assada
[{paoestufa}] Esteiras Estufa
[{paogrande}] Esteiras Grandão
[{askadicional}] Esteiras Adicionais

          [{soma}] ESTEIRAS PARA TIRAR
************************************           
''')
            
            comando= f'INSERT INTO padaria_sup (quantiadia,quantiasobracrua,quantiasobraassada,sobraestufa,adicionais,nograndao,pratirar) VALUES ({catedia},{askcrua},{askassada},{paoestufa},{askadicional},{paogrande},{soma})'    
            cursor.execute(comando)
            conexao.commit()
        if menuoption==4:            
            comando = 'SELECT * FROM padaria_sup WHERE dia >= CURDATE() - INTERVAL 7 DAY ORDER BY quantiadia ASC;'
            #comando= ''
            cursor.execute(comando)
            resultado=cursor.fetchall()
            for linha in resultado:
               print(linha)  

menupadaria()
#sempre tem que ter para encerrar a tarefa do banco de dados
cursor.close()
conexao.close()
