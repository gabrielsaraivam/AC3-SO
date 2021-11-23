from connectdb import *

blue = "\033[1;34;40m"
reset_color = "\033[0m"

print(blue + "Cadastro BID" + reset_color)

opcoesTimes = " 1- São Paulo FC \n 2- Santos FC \n 3- Fortaleza EC \n 4- CR Vasco da Gama\n 5- Sair \n"
opcoesPosicao = " 1-ATA \n 2-MEI \n 3-DEF \n 4-GOL \n"

listaNumeroJogadorSPFC = []
listaNumeroJogadorSFC = []
listaNumeroJogadorFEC = []
listaNumeroJogadorCRV = []

def flush(numeroJogador, nomeJogador, posicaoJogador, fkTime):
    insert_db(numeroJogador, nomeJogador, posicaoJogador, fkTime)

def verificarPosicao(posicaoJogador):
    if posicaoJogador == 1:
        return "ATA"

    elif posicaoJogador == 2:
        return "MEI"

    elif posicaoJogador == 3:
        return "DEF"

    else:
        return "GOL"


def verificarNumero(numeroJogador, valor):
    for i in valor:
        if numeroJogador == i:
            print("Já existe um jogador com este número, tente novamente")
            return False

    return True


def cadastrarJogador(valor, fkTime):
    numeroJogador = int(input("Digite o número do jogador:\n"))

    if verificarNumero(numeroJogador, valor):
        print("Selecione a posição:")
        posicaoJogador = int(input(opcoesPosicao))
        if posicaoJogador>=1 and posicaoJogador<=4:
            nomeJogador = input("Digite o nome do jogador:\n")
            valor.insert(0, numeroJogador)
            flush(numeroJogador, nomeJogador, verificarPosicao(posicaoJogador), fkTime)
        else:
            print("Posição inválida tente novamente")
            cadastrarJogador(valor, fkTime)
        
    else:
        cadastrarJogador(valor, fkTime)


while True:
    print("Selecione o time que contratou o jogador:")
    inputTime = int(input(opcoesTimes))

    if inputTime>=1 and inputTime<=4:
        if inputTime == 1:
            cadastrarJogador(listaNumeroJogadorSPFC, 1)
        
        elif inputTime == 2:
            cadastrarJogador(listaNumeroJogadorSFC, 2)

        elif inputTime == 3:
            cadastrarJogador(listaNumeroJogadorFEC, 3)

        else:
            cadastrarJogador(listaNumeroJogadorCRV, 4)
    
    elif inputTime == 5:
        break

    else:
        print("valor incorreto, tente novamente")



