#listas
frutas = ['laranja','maca','uva']
#frutas[0]
#frutas[1]
#frutas[-1]
#frutas[-3]
letras =list('python')
numeros=list(range(10))
carro= ['ferrari','f8',420000,2020,2900,'sao paulo',True]
option=0
print(frutas[-1])
#lista=['p','y','t','h','o','n']
#lista[2:] t h o n
#lista[:2] p y
#lista[1:3] y t
#lista[0:3:2] p t
#lista[::] p y t h o n
#lista[::-1] n o h t y p
#for carro in carro:
 #    print(carro)

#lista=[]
#lista.append(1) adicionar elementos lista
#lista.append('python')
#print(lista)
#lista.clear() limpar lista
#Lista.copy() copiar lista
#l2 = lista.copy()
#lista.count('vermelho') # 1 contagem items da lista
#linguaguens.extend(['java','csharp']) juntar listas
#linguaguens.index('java') local aonde ta a string ,position
#linguaguens.pop
#linguaguens.remove('c')
#letras=('AJSDAJ') TUPLA NÃO MUDA SÃO UMUTAVEIS
#set([1,2,3,1,3,4])1 2 3 4 < set não se repete
#dicionario dados ={"nome": "guilherme","idade": 28,} imutavel 
# dicionarios aninhados uma estrutura dentro da outra
#dados["nome"]= "guilherme" alterar dados dicionario

#exemplo ={
#"andrematana23@gmail.com": {"nome": "andré leonardo"},
#"jenifermaisa@gmail.com": {"nome": "jenifer maisa"}
# }
#exemplo["andrematana23@gmail.com"]["nome"] recuperar dados do cionario
#exemplo.clear() limpar dados dicionario
#copia = exemplo.copy() copia dicionario
#dict.fromkeys(["nome","telefone"],"vazio") criar chaves dentro de dicionarios
#exemplo.get("andrematana23@gmail.com,",{}) ver dados do dicionario
#exemplo.pop("andrematana23@gmail.com",{}) remover dados da chave
#in exemplo verificar se existe chave no dicionario

#for chave in contatos:
#print(chave,contatos[chave])
#for chave,valor in contatos.items():
#print(chave,valor)
#**********************************

#muito top funçãos
def exibir_mensagem():
      print(f'Olá Mundo! {nome}')
     #cria definição e uma estrutura pré definida
exibir_mensagem(nome="andré")

def calcular_total(numeros):
      return sum(numeros)
print(calcular_total([10,20,34]))

def savar_carro(marca,modelo,ano,placa):
      print(f'carro inserido com sucesso',{marca},{modelo},{ano},{placa})
savar_carro('fiat','palio',1999,'abc-1234')
savar_carro(marca="fiat",modelo='palio')
savar_carro(**{'marca':'fiat'})





if option==3:    
     #classe string manipular
     curso ='   p Y t h O n'
     menu='Menu'
     print(curso.upper()) #tudo maisculo
     print(curso.lower()) #tudo minusculo
     print(curso.title())#primeira letra maiuscula
     print(curso.capitalize())
     print(curso.strip())#tirar espaços
     print(curso.lstrip())#tirar espaços esquerda
     print(curso.rstrip())#tirar espaços a direita
     print(curso.center(10,'#')) 
     print('.'.join(curso))
     print( menu.center(30,'*'))
     nome='André Leonardo de lima'
     idade=28
     profissao='Programador'
     pi= 3.14159

     print('Olá Me Chamo %s.eu tenho %d anos de idade,trabalhando de %s' % (nome,idade,profissao)) #old style
     print('Olá Me Chamo {}.eu tenho {} anos de idade,trabalhando de {}' .format(nome,idade,profissao)) #quase old
     print(f'Olá Me Chamo {nome}.eu tenho {idade} anos de idade,trabalhando de {profissao}') #meior
     print(f'Valor de pi {pi:.2f}')
     print(f'Valor de pi {pi:10.2f}')
#fatiamento strings
     la='Comedor de viado'
     print(nome[0:5])
     print(nome[6:15])
     print('Seja Bem Vindo',nome,la[0:7])















