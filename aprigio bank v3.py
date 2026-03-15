from colorama import Fore,Style,init
from time import sleep
from datetime import date,datetime

init(autoreset=True)

usuarios = []

# ================= CADASTRO =================

def cadastrar():

    nome=input('Qual o seu nome?')

    while True:

        usuario=input('Crie um usuario:')
        usuario_existe=False

        for pessoa in usuarios:

            if usuario == pessoa['usuario']:
                print(Fore.RED+'Já existe um usuário com esse nome')
                usuario_existe=True
                break

        if usuario_existe:
            continue

        senha=input('Crie uma senha:')

        novo_usuario={
            'nome':nome,
            'usuario':usuario,
            'senha':senha,
            'saldo':0,
            'extrato':[]
        }

        usuarios.append(novo_usuario)

        print(Fore.GREEN+'Conta criada com sucesso!')
        break


# ================= LOGIN =================

def login():

    print(Style.BRIGHT+'ACESSE SUA CONTA')

    while True:

        usuario=input('Digite seu usuário:')
        usuario_existe=False

        for pessoa in usuarios:

            if usuario == pessoa['usuario']:

                usuario_existe=True
                senha=input('Digite sua senha:')

                if senha == pessoa['senha']:

                    print(Fore.GREEN+'LOGIN REALIZADO!')
                    return pessoa

                else:

                    print(Fore.RED+'Senha incorreta!')
                    return None

        if not usuario_existe:

            print(Fore.RED+'Usuário não encontrado')
            return None


# ================= BANCO =================

def depositar(usuario):

    try:

        valor=float(input('Valor do depósito R$:'))

        agora=datetime.now()
        data_formatada=agora.strftime('%d/%m/%Y %H:%M')

        if valor<=0:

            print(Fore.RED+'Valor inválido')

        else:

            usuario['saldo']+=valor

            usuario['extrato'].append(
                Fore.GREEN+'{} | DEPÓSITO | R${:.2f}'.format(data_formatada,valor)
            )

            print(Fore.GREEN+'Depósito realizado!')
            print('Saldo atual R${:.2f}'.format(usuario['saldo']))

    except:

        print('Digite apenas números')


def sacar(usuario):

    try:

        valor=float(input('Valor do saque R$:'))

        agora=datetime.now()
        data_formatada=agora.strftime('%d/%m/%Y %H:%M')

        if valor<=0:

            print(Fore.RED+'Valor inválido')

        elif valor>usuario['saldo']:

            print(Fore.RED+'Saldo insuficiente')

        else:

            usuario['saldo']-=valor

            usuario['extrato'].append(
                Fore.RED+'{} | SAQUE | R$-{:.2f}'.format(data_formatada,valor)
            )

            print(Fore.GREEN+'Saque realizado!')
            print('Saldo atual R${:.2f}'.format(usuario['saldo']))

    except:

        print('Digite apenas números')


def ver_carteira(usuario):

    print(Style.BRIGHT+'SALDO ATUAL: R${:.2f}'.format(usuario['saldo']))
    print('===EXTRATO===')

    if not usuario['extrato']:

        print('SEM MOVIMENTAÇÕES')

    else:

        for item in usuario['extrato']:
            print(item)


# ================= MENU DO BANCO =================

def menu_banco(usuario):

    while True:

        print('\n=== APRIGIO BANK$ ===')

        print('1 Depositar')
        print('2 Sacar')
        print('3 Ver carteira')
        print('4 Logout')

        escolha=input('Escolha: ').strip().lower()

        if escolha in ['1','depositar']:

            depositar(usuario)

        elif escolha in ['2','sacar']:

            sacar(usuario)

        elif escolha in ['3','ver','carteira']:

            ver_carteira(usuario)

        elif escolha in ['4','logout']:

            print('Saindo da conta...')
            break

        else:

            print('Opção inválida')


# ================= MENU PRINCIPAL =================

while True:

    print('\nBem-vindo ao AprigioBank$')

    print('1 Cadastrar')
    print('2 Login')
    print('3 Sair')

    menu=input('Escolha: ').strip().lower()

    if menu in ['1','cadastrar']:

        cadastrar()

    elif menu in ['2','login']:

        usuario_logado=login()

        if usuario_logado:

            menu_banco(usuario_logado)

    elif menu in ['3','sair']:

        print('Encerrando sistema...')
        break

    else:

        print('Opção inválida')