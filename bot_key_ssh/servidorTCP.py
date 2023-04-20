# importacao das bibliotecas
from socket import * # sockets
import subprocess
import pickle

# definicao das variaveis
#serverName = '192.168.100.7' # ip do servidor (em branco)
serverName = ''
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))


while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  recv = connectionSocket.recv(2048) # recebe dados do cliente
  dados = pickle.loads(recv)
  
  comando = str("git config --global user.name " + "\"" + dados["user_name"] + "\"" + "&&" + " git config --global user.email " + "\"" + dados["user_email"] + "\"" + "&&" + " ssh-keygen -t ed25519 -C " + "\"" + dados["user_email"] + "\"")
  
  
  
  resposta = subprocess.check_output(comando, shell=True, universal_newlines=True, 
stderr=subprocess.STDOUT)

  connectionSocket.send(resposta.encode('utf-8')) # envia para o cliente o texto transformado
  connectionSocket.close() # encerra o socket com o cliente
serverSocket.close() # encerra o socket do servidor