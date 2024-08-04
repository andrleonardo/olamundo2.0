import datetime
mes = datetime.date.today()
diain = datetime.date.today().weekday()
dias_da_semana = ['Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sabado', 'Domingo']
dia = dias_da_semana[diain] if 0 <= diain <= 6 else 'Bug'

# Dicionário de login e saldos
dictlogin = {'04466655556': {'nome': 'André Leonardo De Lima Matana', 'senha': 'leleo', 'saldo': 1000}}

def valida_cpf(cpf: str) -> bool:
    """Valida se o CPF tem 11 dígitos"""
    cpf = ''.join(filter(str.isdigit, cpf))
    return len(cpf) == 11

def cadastrarcheck():
    """Função para cadastrar um novo usuário"""
    print('''
***********************************
        Ficamos Muito Feliz 
    em saber que quer participar
***********************************''')
    askcpf = input('Qual seu CPF? [Sem ponto e espaço] ').strip()
    
    if askcpf in dictlogin:
        print('Já existe seu CPF no nosso sistema!!')
    elif valida_cpf(askcpf):
        nome = input("Digite seu nome completo: ").strip()
        senha = input("Digite uma senha: ").strip()
        dictlogin[askcpf] = {'nome': nome, 'senha': senha, 'saldo': 0}
        print(f'Cadastro realizado com sucesso, {nome}!')
    else:
        print('CPF INVÁLIDO')

def fazer_login():
    """Função para login do usuário"""
    askcpf = input('Digite seu CPF: [Sem ponto e espaço] ').strip()
    senha = input('Digite sua senha: ').strip()
    
    if askcpf in dictlogin and dictlogin[askcpf]['senha'] == senha:
        print(f'Bem-vindo, {dictlogin[askcpf]["nome"]}!')
        return askcpf
    else:
        print('CPF ou senha incorretos')
        return None

def mostrar_saldo(cpf):
    """Função para mostrar o saldo do usuário"""
    saldo = dictlogin[cpf]['saldo']
    print(f'Seu saldo atual é: R${saldo:.2f}')

def sacar(cpf):
    """Função para saque"""
    valor = float(input('Digite o valor para sacar: R$'))
    if valor <= dictlogin[cpf]['saldo']:
        dictlogin[cpf]['saldo'] -= valor
        print(f'Saque de R${valor:.2f} realizado com sucesso.')
    else:
        print('Saldo insuficiente.')

def depositar(cpf):
    """Função para depósito"""
    valor = float(input('Digite o valor para depositar: R$'))
    dictlogin[cpf]['saldo'] += valor
    print(f'Depósito de R${valor:.2f} realizado com sucesso.')

def transferir(cpf):
    """Função para transferência"""
    cpf_destino = input('Digite o CPF do destinatário: [Sem ponto e espaço] ').strip()
    
    if cpf_destino in dictlogin:
        valor = float(input('Digite o valor para transferir: R$'))
        if valor <= dictlogin[cpf]['saldo']:
            dictlogin[cpf]['saldo'] -= valor
            dictlogin[cpf_destino]['saldo'] += valor
            print(f'Transferência de R${valor:.2f} para {dictlogin[cpf_destino]["nome"]} realizada com sucesso.')
        else:
            print('Saldo insuficiente.')
    else:
        print('CPF do destinatário não encontrado.')

def consultar_cadastros():
    """Função para consultar todos os cadastros"""
    print('Cadastros no sistema:')
    for cpf, dados in dictlogin.items():
        print(f'CPF: {cpf}, Nome: {dados["nome"]}, Saldo: R${dados["saldo"]:.2f}')

def menu_bancario(cpf):
    """Menu para operações bancárias"""
    while True:
        opcao = int(input('''
*********************************************************
*            * O P E R A Ç Õ E S   B A N C Á R I A S *  *
*********************************************************
* [1] Mostrar Saldo                                      *
* [2] Sacar                                              *
* [3] Depositar                                          *
* [4] Transferir                                         *
* [5] Sair                                               *
*********************************************************
>> '''))
        if opcao == 1:
            mostrar_saldo(cpf)
        elif opcao == 2:
            sacar(cpf)
        elif opcao == 3:
            depositar(cpf)
        elif opcao == 4:
            transferir(cpf)
        elif opcao == 5:
            print('Até mais!')
            break
        else:
            print('Opção inválida.')
while True:
    menuoptionlogin = int(input(f'''
*********************************************************
*           * M E N U    B A N C O   L E L E O *        *
* {dia} - {mes}        ************                      *
*********************************************************                                                          
* [1] Se Cadastrar             [3] Consultar Cadastros   *
* [2] Fazer Login              [4] Sair                 *
*********************************************************
>> '''))
    
    if menuoptionlogin == 1:
        cadastrarcheck()
    elif menuoptionlogin == 2:
        usuario_logado = fazer_login()
        if usuario_logado:
            menu_bancario(usuario_logado)
    elif menuoptionlogin == 3:
        consultar_cadastros()
    elif menuoptionlogin == 4:
        print('Até mais!')
        break
    else:
        print('Opção inválida.')
