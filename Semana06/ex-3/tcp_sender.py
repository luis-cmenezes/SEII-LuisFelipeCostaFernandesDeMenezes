import socket # Módulo de comunicação de rede
import sys # Interação na chamada do código

TCP_IP = "127.0.0.1" # Define o endereço IP do servidor TCP
FILE_PORT = 5005 # Define a porta para o envio do nome do arquivo
DATA_PORT = 5006 # Define a porta para envio dos dados do arquivo
file_name = sys.argv[1] # Recebe o nome do arquivo na chamada do código


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria socket TCP
    sock.connect((TCP_IP, FILE_PORT)) # Conecta ao receiver na porta do nome do arquivo
    sock.send(('sendtcp_'+file_name).encode()) # Encoda e envia o nome do arquivo
    sock.close() # Encerra a comunicação do nome do arquivo
 
    print(f"Sending %s ... {file_name}") # Indica que o arquivo está sendo enviado

    f = open(file_name, "rb") # Lê o arquivo em modo binário
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Novo socket TCP
    sock.connect((TCP_IP, DATA_PORT)) # Conecta ao receiver na porta de dados do arquivo
    data = f.read() # Lê o arquivo
    sock.send(data) # Envia os dados pelo socket

finally:
    sock.close() # Encerra a comunicação dos dados do arquivo
    f.close() # Fecha o arquivo