import socket # Módulo de comunicação de rede
import time # Controle de tempo
import sys # Interação na chamada do código

UDP_IP = "127.0.0.1"  # Define o endereço IP do servidor UDP
UDP_PORT = 5005 # Define a porta do servidor UDP
buf = 1024 # Tamanho do buffer para leitura de dados do socket
file_name = sys.argv[1] #  Recebe o nome do arquivo na chamada do código


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria um socket para UDP
sock.sendto(('sendudp_'+file_name).encode(), (UDP_IP, UDP_PORT))  # Envia uma mensagem indicando o início do envio do arquivo e seu nome
print(f"Sending %s ... {file_name}") # Indica o início do envio
 
f = open(file_name, "rb") # Lê o arquivo em modo binário
data = f.read(buf) # Lê o arquivo até o tamanho do buffer
while(data): # Loop enquanto houver dados não enviados no arquivo
    if(sock.sendto(data, (UDP_IP, UDP_PORT))): # Envia os dados para receiver UDP
        data = f.read(buf) # Lê o restante do arquivo até o tamanho do buffer
        time.sleep(0.02) # Dá um intervalo para o receiver salvar os dados

sock.close() # Encerra a comunicação
f.close() # Fecha o arquivo