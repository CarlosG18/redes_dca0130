# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Base de um servidor HTTP (python 3)
#

# importacao das bibliotecas
import socket
import os

# definicao do host e da porta do servidor
HOST = '' # ip do servidor (em branco)
PORT = 8080 # porta do servidor

# cria o socket com IPv4 (AF_INET) usando TCP (SOCK_STREAM)
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# permite que seja possivel reusar o endereco e porta do servidor caso seja encerrado incorretamente
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# vincula o socket com a porta (faz o "bind" do IP do servidor com a porta)
listen_socket.bind((HOST, PORT))

# "escuta" pedidos na porta do socket do servidor
listen_socket.listen(1)

# imprime que o servidor esta pronto para receber conexoes
print ('Serving HTTP on port %s ...' % PORT)

def file_content(file_path):
  if os.path.exists(file_path):
    file = open(file_path, "rb")
    content = file.read()
    return content.decode('utf-8'), True
  else:
    content = """
<html>
  <head></head>
  <body>
    <h1>404 Not Found</h1>
  </body>
</html>
"""
    return content, False

while True:
    # aguarda por novas conexoes
    client_connection, client_address = listen_socket.accept()
    # o metodo .recv recebe os dados enviados por um cliente atraves do socket
    request = client_connection.recv(1024)
    str_request = request.decode('utf-8')
    print(str_request)
    
    message_ok = "HTTP/1.1 200 OK"
    message_not_found = "HTTP/1.1 404 Not Found"
    message_bad_request = "HTTP/1.1 400 Bad Request"
    
    x = str_request.split(" ")
    
    if x[0] == "GET":
      path = "."+x[1]
      if path == "./":
        content, exists = file_content("./index.html")
        if exists:
          message_http = message_ok
        else:
          message_http = message_not_found
      else:
        content, exists = file_content(path)
        if exists:
          message_http = message_ok
        else:
          message_http = message_not_found
    else:
        message_http = message_bad_request
        content = """
<html>
  <head></head>
  <body>
    <h1>400 Bad Resquest</h1>
  </body>
</html>
"""
    
    http_response = f"""\
{message_http}

{content}
"""
    
    # declaracao da resposta do servidor
    # servidor retorna o que foi solicitado pelo cliente (neste caso a resposta e generica)
    client_connection.send(http_response.encode('utf-8'))
    # encerra a conexao
    client_connection.close()

# encerra o socket do servidor
listen_socket.close()