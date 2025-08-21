# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
# MODIFICADO POR ALUNO: CARLOS GABRIEL MEDEIROS DA SILVAs 
# TURMA: 

# Tarefa A: Desenvolver um servidor de data
# Faça as alterações necessárias nos códigos fonte para que o cliente envie uma solicitação ao servidor e este responda com a data e o horário do sistema.
# a. Implemente utilizando sockets UDP;
# b. Importe a biblioteca time e utilize o método time.ctime() para capturar a hora;
# c. Atente que será necessário converter o método time.ctime() em string por meio do método str(): str(time.ctime())
# d. O cliente deve digitar o comando: data e aguardar o servidor responder com a data. Outros comandos não devem ser aceitos.

# importacao das bibliotecas
from socket import * # sockets
from time import ctime

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP
serverSocket.bind((serverName, serverPort)) # bind do ip do servidor com a porta
print ('Servidor UDP esperando conexoes na porta %d ...' % (serverPort))

while 1:
    comando, clientAddress = serverSocket.recvfrom(2048) # recebe do cliente
    if comando.decode('utf-8') == "data":
      data = str(ctime())
      print ('Cliente %s enviou: %s e retorna a data: %s' % (clientAddress, comando, data))
      serverSocket.sendto(data.encode('utf-8'), clientAddress)
    else:
      error = "comando não válido"
      serverSocket.sendto(error.encode('utf-8'), clientAddress) 
# envia a resposta para o cliente
serverSocket.close() # encerra o socket do servidor