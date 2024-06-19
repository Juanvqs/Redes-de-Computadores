from socket import *
import os

def mostrar_oJogo(oJogo):
    for i in range(0,3):
        print("%d %d %d" % (oJogo[i][0],oJogo[i][1],oJogo[i][2]))

def main():
    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    oJogo = [[0,0,0],[0,0,0],[0,0,0]]
    while 1:
        os.system("clear")
        mostrar_oJogo(oJogo)

        x, y = input('Jogada:')
        # x, y = str(jogada).split(",")
        #
        # x = int(x)
        # y = int(y)
        oJogo[x-1][y-1] = 2

        jogada = "%d,%d"%(x,y)

        clientSocket.send(jogada.encode())

        jogada = clientSocket.recv(3).decode()

        print(jogada)
        x, y = jogada.split(",")

        x = int(x)
        y = int(y)
        oJogo[x-1][y-1] = 1

    clientSocket.close()

if __name__ == "__main__":
        main()
