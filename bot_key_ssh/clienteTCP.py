# importacao das bibliotecas
from socket import *
import pickle

# definicao das variaveis
#serverName = '192.168.100.7' # ip do servidor
serverName = 'localhost'
serverPort = 61000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

#dados do git
user_name = input("insira seu user_name: ")
user_email = input("insira seu user_email: ")
password = input("insira sua senha: ")

dados = {
  "user_name": user_name,
  "user_email": user_email,
  "password": password,
}

serial_data = pickle.dumps(dados)

clientSocket.send(serial_data) # envia o texto para o servidor
resposta = clientSocket.recv(2048) # recebe do servidor a resposta
print ('O servidor (\'%s\', %d) respondeu com:\n%s' % (serverName, serverPort, resposta.decode('utf-8')))
clientSocket.close() # encerramento o socket do cliente
