# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Cliente de sockets TCP modificado para enviar texto minusculo ao servidor e aguardar resposta em maiuscula (python 3)
#

# importacao das bibliotecas
from socket import *
import pickle

# definicao das variaveis
serverName = 'localhost' # ip do servidor
serverPort = 61000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor


comando = input('Digite o comando: ')
arquivo = input('Digite o nome do arquivo: ')
dados = {
  "comando": comando,
  "arquivo": arquivo,
}

#serializar o objeto
serial_dados = pickle.dumps(dados)

clientSocket.send(serial_dados) # envia o comando para o servidor
data_file = clientSocket.recv(1024) # recebe do servidor o conteudo do arquivo
print ('O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, data_file.decode('utf-8')))
clientSocket.close() # encerramento o socket do cliente