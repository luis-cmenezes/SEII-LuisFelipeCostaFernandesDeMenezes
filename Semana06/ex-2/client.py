import socket

# Definição dos mesmos parâmetros que no server
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um socket para o cliente
client.connect(ADDR) # Conecta ao servidor

def send(msg):
    message = msg.encode(FORMAT) # Codifica a mensagem
    msg_length = len(message) # Tamanho da mensagem codificada

    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length)) # Preenche o cabeçalho com o tamanho correto

    client.send(send_length) # Envia o header
    client.send(message) # Envia a mensagem

    print(client.recv(2048).decode(FORMAT)) # Confirmação do servidor

send("Hello World!")
input() # Aguarda entrada do usuário antes de enviar a próxima mensagem
send("Hello World! 2")
input()
send("Hello World! 3")
input()

send(DISCONNECT_MSG) # Disconecta do servidor