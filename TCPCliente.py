from socket import *

oJogo = [3 * [0], 3 * [0], 3 * [0]]

serverName = 'localhost'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

tem_jogo = True

while(tem_jogo):
    x = int(input())
    y = int(input())

    oJogo[x][y] = 2 #Jogada do cliente
    jogada = "%d|%d" % (x, y)
    tem_jogo = tem_jogo_ainda(oJogo)

    clientSocket.send(jogada.encode())

    if(tem_jogo):
        jogada_do_outro = clientSocket.recv(1024).decode()

        print('Do servidor: %s' % jogada_do_outro)

        xx, yy = jogada_do_outro.split("|")
        x = int(xx)
        y = int(yy)

        oJogo[x][y] = 1 #Jogada do servidor
        tem_jogo = tem_jogo_ainda(oJogo)

clientSocket.close()
