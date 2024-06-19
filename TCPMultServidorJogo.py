from socket import *
from random import *
import threading

def verifica_jogo(ojogo):
    if (ojogo[0][0] == ojogo[1][1]) and (ojogo[0][0] == ojogo[2][2]) and (ojogo[0][0] != 0):
        return True, False

    if (ojogo[0][2] == ojogo[1][1]) and (ojogo[0][2] == ojogo[2][0]) and (ojogo[0][2] != 0):
        return True, False

    for i in range(0,3):
        if (ojogo[i][0] == ojogo[i][1]) and (ojogo[i][0] == ojogo[i][2]) and (ojogo[i][0] != 0):
            return True, False

    for j in range(0,3):
        if (ojogo[0][j] == ojogo[1][j]) and (ojogo[0][j] == ojogo[2][j]) and (ojogo[0][j] != 0):
            return True, False

    for i in range(0,3):
        for j in range(0,3):
            if (ojogo[i][j] == 0):
                return False, False

    return False, True

def valida_jogada(ojogo, x, y, jogador):
     if (ojogo[x][y] != 0):
         return False
     else:
         ojogo[x][y] = jogador
         return True

def euJogando(oJogo):
    x = randint(0,2)
    y = randint(0,2)
    while not (valida_jogada(oJogo, x, y, jogador=1)):
        x = randint(0,2)
        y = randint(0,2)

    return x,y

def mostrar_oJogo(oJogo):
    for i in range(0,3):
        print("%d %d %d" % (oJogo[i][0],oJogo[i][1],oJogo[i][2]))


def atende_cliente(connectionSocket):
    ojogo=[[0,0,0],[0,0,0],[0,0,0]]
    velhou = False
    temvencedor = False

    while (not velhou) and (not temvencedor):
        jogada = connectionSocket.recv(4).decode()

        print("---------%s"%jogada)

        x,y = jogada.split(',')
        if valida_jogada(ojogo, int(x)-1, int(y)-1, jogador=2):

            mostrar_oJogo(ojogo)

            temvencedor, velhou = verifica_jogo(ojogo)
            if ( not temvencedor) and ( not velhou):
                mX, mY = euJogando(ojogo)
                temvencedor, velhou = verifica_jogo(ojogo)
                if ( not temvencedor) and ( not velhou):
                    jogada = "%d,%d"%(mX+1,mY+1)
                    connectionSocket.send(jogada.encode())
                elif(velhou):
                    print("Velhou, sem ganhador")
                elif(temvencedor):
                    print("Eu venci o jogo, Parabéns!!!")

            elif (velhou):
                print("Velhou, sem ganhador")
            elif(temvencedor):
                print("Você venceu o jogo, Parabéns!!!")

    connectionSocket.close()
    print("Encerrando o atendimento do cliente")

def main():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print('Servidor pronto')
    while 1:
        connectionSocket, addr = serverSocket.accept()
        print("Cliente: endereco %s e Porta %s:" % (addr[0], addr[1]))
        #atende_cliente(connectionSocket)
        x = threading.Thread(target=atende_cliente, args=(connectionSocket,))
        print("Iniciando atendimento do Cliente")
        x.start()

    serverSocket.close()


if __name__=='__main__':
    main()
