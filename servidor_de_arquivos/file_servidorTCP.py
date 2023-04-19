# aluno: carlos gabriel medeiros da silva 
#turma: 
#disciplina:

# Tarefa B: Desenvolver um servidor de arquivos
# Faça as alterações necessárias nos códigos fonte para que o cliente envie uma solicitação ao servidor e este responda com conteúdo de um arquivo texto.
# a. Implemente utilizando sockets TCP;
# b. Crie um arquivo de texto simples (por exemplo: arquivo.txt) e escreva alguma informação em 1 linha nesse arquivo;
# c. Faça com que o servidor leia o arquivo (local) e retorne o seu conteúdo para o cliente quando este digitar o comando: obter arquivo.txt. Outros comandos não devem ser aceitos;
# d. Use o método open(arquivo.txt) para abrir o arquivo solicitado e o método .read() para ler o seu conteúdo.

# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Servidor de sockets TCP modificado para receber texto minusculo do cliente enviar resposta em maiuscula  (python 3)
#

# importacao das bibliotecas
from socket import * # sockets

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  sentence = connectionSocket.recv(1024) # recebe dados do cliente
  sentence = sentence.decode('utf-8')
  capitalizedSentence = sentence.upper() # converte em letras maiusculas
  print ('Cliente %s enviou: %s, transformando em: %s' % (addr, sentence, capitalizedSentence))
  connectionSocket.send(capitalizedSentence.encode('utf-8')) # envia para o cliente o texto transformado
  connectionSocket.close() # encerra o socket com o cliente
serverSocket.close() # encerra o socket do servidor