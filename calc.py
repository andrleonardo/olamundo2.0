import math
import pywhatkit.whats
import requests
import random
import pywhatkit

class calc:
    def parouimpar():
        num=int(input('Digite Um numero pra saber se é par '))
        resultado=num % 2             # se o resto da divisão por igual a 0 é par
                                  # operador % pega o resto da divisão
        if resultado==0:
            print(f'Seu Número {num} é par')
        else:
            print(f'Seu Número {num} é impar')
    
    def dissecandoumavariavel():
        variavel=str(input('Qual Variavel Você Quer Dissecar? '))
        alphanumerico=variavel.isalpha()
        enumero=variavel.isnumeric()
        espaçado=variavel.isspace()
        maisculo=variavel.isupper()
        minusculo=variavel.islower()
        print(f'''
************************************
VARIAVEL:  {variavel}

Alphanumerico: {alphanumerico}
é numerico: {enumero}
é espaçado: {espaçado}
é maisculo: {maisculo}
é minusculo: {minusculo}
Entre muitos outros.
*************************************
''')
    def sucessoreantecessor():
        num=int(input('Qual Numero você quer saber o sucessor e o antecessor?? '))
        numsucessor= num + 1
        numantecessor=num -1
        print(f'''
******************************************************************************
Do Número {num} o Sucessor é {numsucessor} e o antecessor é {numantecessor}
******************************************************************************
''')
    def dobrotriploraizquadrada():
        num=int(input('Qual Número? '))
        numdobro=num * 2
        numtriplo=num * 3
        numraiz= num** (1/2) #num elevar um numero a potencia de um e meio é o mesmo que raiz quadrada
        #numraiz=math.sqrt(num) Com Biblioteca math
        print(f'O dobro é {numdobro} o triplo é {numtriplo} a raiz quadrada é {numraiz}')
    
    def mediaaritimetica():
        nota1=int(input('Nota 1? '))
        nota2=int(input('Nota 2? '))
        resultado=(nota1 + nota2) /2 #a média aritimetica é feita somando as notas e dividindo por 2 no final
        print(f'A média Aritmetica é {resultado}')
    def conversormedidas():
        num=int(input('Quantos Metros Quer converter? '))
        km=num /1000
        cm=num*100
        mm=num*1000
        print(f'''
km {km}
metro {num}
cm {cm}
mm {mm}
''')
    def cotaçãomoeda():
            ask=0
            req=requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
            req_dic = req.json()
            cotacao_dolar=float(req_dic['USDBRL']['bid'])
            cotacao_euro=float (req_dic['EURBRL']['bid'])
            cotacao_btc=float (req_dic['BTCBRL']['bid'])
            print(f'''
*********************************
    C O T A  M O E D A S:

DOLAR VALENDO = {cotacao_dolar}
EURO VALENDO = {cotacao_euro}
BIT COIN VALENDO = {cotacao_btc}
*********************************
''')
            try:
                askcota=int(input('Deseja transformar algum valor em real para alguma moeda? 1 = sim 2 = não'))

            except ValueError:
                    print('Bota valor valido ai poh')

            if askcota >=2:
                print('ok fechando')
            elif askcota==1:
                askreal=float(input('Quantos Reais Deseja Converter?'))
                askmoeda=int(input('''
**********************
[1] REAL PARA DOLAR
[2] REAL PARA EURO 
[3] REAL PARA BITCOIN
***********************'''))
                try:
                    if askmoeda==1:
                     real=askreal/cotacao_dolar

                    elif askmoeda==2:
                        real=askreal / cotacao_euro
                    elif askmoeda==3:
                        real=askreal / cotacao_btc
                except ValueError:
                    print('Bota valor valido ai poh')
                print(f'O VALOR DE REAL PARA A MOEDA DA ESCOLHA É {real:.2f}')
    def localizacep():
        cpe=str(input('Qual CPE DESEJA O ENDEREÇO? '))
        req=requests.get(f'https://cep.awesomeapi.com.br/json/{cpe}')
        convert=req.json()
        rua=convert['address_name']
        estado=convert['state']
        cidade=convert['city']
        print(f'''
*******************************
        CPE {cpe}

rua={rua}
estado={estado}
cidade={cidade}
********************************
''')
    
    def reajustesalario():
        asksalario=float(input('Qual Seu Salário? '))
        askporcento=float(input('Quantos porcento de Reajuste? '))
        resultado= asksalario + (asksalario *askporcento/100)
        print(resultado)
    def conversortemperaura():
        graus=float(input('Quantos graus Celsius para fahr quer converter? '))
        resultado=((graus* 9 )/5) +32
        print(resultado)
    def aluguelcarro():
        kmrodado=float(input('Quantos KM rodados? '))
        dias=float(input('Quantos dias? '))
        resultado=(kmrodado * 0.15) + (dias * 60)
        print(resultado)
    def quebrandoumnumero():
        numero=float(input('Qual Numero? '))
        print(f'o numero é {numero:.0f}')
    def hipotenusa():
        co=float(input('Qual o cateto oposto? '))                     #cateto oposto
        ca=float(input('Qual o cateto adjascente? '))                #cateto adjacente
        hi= (co ** 2+ ca **2) **(1/2) #igual o ao quadrado porem soma todos 
        print(f'A hipotenusa vai medir {hi}')
    def senocossenoetangente():
        angulo=float(input('Digite um angulo que vocÊ deseja? '))
        seno=math.sin(math.radians(angulo))
        print(f'você tem um seno de {seno}')
        cosseno=math.cos(math.radians(angulo))
        print(f'vocÊ tem o cosseno de {cosseno}')
        tan=math.tan(math.radians(angulo))
        print(f'a tangente tem o valor de {tan}')
    def sortenadolista():
        lista=['banana','batata','tomate']
        print(lista[random.randint(0,2)])
    
    #TUPLAS
    
    
    
    
    
    
    
    
    
    
    def sorteandolistatd():#                                 IMCOMPLETO!!!
        option=5
        aluno1=str(input('Qual O Nome do primeiro aluno? '))
        aluno2=str(input('Qual o Nome do segundo aluno? '))
        alunos= ['','','','','','',aluno1,aluno2]
        while option >2:
            askmore=int(input('Deseja ADD MAIS? 1 =SIM 2 = NÃO'))
            if askmore==1:
                alunos=input('Qual Mais? ')
                print(alunos)

    def numeroporextenso():
        num=int(input('Qual numero deseja por extenso? 0/10 '))    
        tupla=('Zero','Um','Dois','TrÊs','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez')
        print(tupla[num]) # modo bonito!
        #if num ==0:            ifs feio pra caralho
         #   print(tupla[0])
        #elif num==1:
        #    print(tupla[1])
        #elif num==2:
        #    print(tupla[2])
        #elif num==3:
        #    print(tupla[3])
        #elif num==4:
        #    print(tupla[4])
        #elif num==5:
        #    print(tupla[5])
        #elif num==6:
        #    print(tupla[6])
        #elif num==7:
        #     print(tupla[7])
        #elif num==8:
        #    print(tupla[8])
        #elif num==9:
        #    print(tupla[9])
        #elif num==10:
        #    print(tupla[10])

    def sortear5numeroseordenando():
        numeros=(random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
        print(numeros)
        for n in numeros:
            print(n)
        print(f'O MAIOR NUMERO É {max(numeros)}',end='') # estudar oq é esse end do caralho ai
        print(f'o menor numero é {min(numeros)}')

    def whats():
        import timer
        import pywhatkit
        import mysql.connector
        conexao=mysql.connector.connect(
        host='localhost'
        ,user='root'
        ,password='P1zzaateotalo'
        ,database='bancodoleo')
        
        cursor=conexao.cursor()
        
        query = """
            SELECT mf.materias, p.tipoprova, p.peso, p.datafazer, p.datafim
            FROM provas p
            JOIN materiasfacul mf ON p.materia = mf.id
            WHERE p.datafazer >= CURDATE()
            ORDER BY p.datafazer ASC;
            """
        cursor.execute(query)
        resultados = cursor.fetchall()
            
        if resultados:
            print("Próximas provas:")
            for  row in resultados:
                print(f"{row[0]}, {row[1]}, VALE {row[2]}, DATAFAZER {row[3].strftime('%d/%m/%Y')}, DATAFIM {row[4].strftime('%d/%m/%Y')}")
              
            else:
                print("Nenhuma prova futura encontrada.")





        number='+(55) 55 996595524'
        #message= f'''{row[0]},{row[1],{row[2]}} '''
        pywhatkit.sendwhatmsg_instantly(number,print)
        cursor.close()
        conexao.close()
    def juros_whats():
        
        try:
            valor_produto=float(input('Qual O Valor do produto? '))
        except ValueError:
            print('Valor Valido Porfavor')
        try:
            quantas_parcelas=int(input('Quantas parcelas? '))
        except:
            print('Valor Valido Por FAVOR')

        if quantas_parcelas<=4:
               juros=0.5
        elif quantas_parcelas >=4:
               juros=0.5 #%
        else:
           print('valor errado')
        valor_parcela= valor_produto / quantas_parcelas
        juros_parcela= valor_parcela + (valor_parcela* juros)
        valor_total=juros_parcela * quantas_parcelas   
        valor_total_sj=valor_parcela * quantas_parcelas
        print(f'''
***********************
valor parcelado s/j:{valor_parcela:.2f}
Valor Parcelado c/j: {juros_parcela:.2f} 
valor total c/j:{valor_total:.2f}
valor total s/j:{valor_total_sj:.2f}
''')
        numero='+(55) 55 996595524'
        message=f'o valor parcelado do seu produto ficou {valor_parcela}'
        pywhatkit.whats.sendwhatmsg_instantly(numero,message)
    
        


