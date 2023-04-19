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
serverName = 'localhost' # ip do servidor a se conectar
serverPort = 61000 # porta a se conectar
clientSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP

comando = input('Digite o comando data: ')
clientSocket.sendto(comando.encode('utf-8'),(serverName, serverPort)) # envia mensagem para o servidor
data, serverAddress = clientSocket.recvfrom(2048) # recebe do servidor a resposta
print ('O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, data.decode('utf-8')))
clientSocket.close() # encerra o socket do cliente