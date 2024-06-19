from socket import *
import threading

def main():
    oJogo = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    serverPort = 12001
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)

    print('Servidor do Hellmut pronto')

    while 1:
        connectionSocket, addr = serverSocket.accept()
        while(tem_jogo):
            print("Cliente: endereco %s e Porta %s:" % (addr[0], addr[1]))
            jogada = connectionSocket.recv(1024).decode()

            xx, yy = jogada.split("|")
            x = int(xx)
            y = int(yy)

            oJogo[x][y] = 2 #Jogada do cliente
            print(oJogo)

            x = int(input())
            y = int(input())
            
            oJogo[x][y] = 1 #Jogada do servidor

            jogada = "%d|%d" % (x, y)

            connectionSocket.send(jogada.encode())
        connectionSocket.close()

    print("Encerrando o atendimento do cliente")

    serverSocket.close()


if __name__=='__main__':
    main()
