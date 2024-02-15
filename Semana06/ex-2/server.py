import socket # Módulo para comunicação via socket
import threading # Módulo para threads

HEADER = 64 # Tamanho do cabeçalho da mensagem
PORT = 5050 # Porta em que o servidor irá receber conexões
SERVER = socket.gethostbyname(socket.gethostname()) # Obtém o endereço de IP do server
ADDR = (SERVER, PORT) 
FORMAT = 'utf-8' # Formato para codificação das mensagens
DISCONNECT_MSG = "!DISCONNECT" # Mensagem do client para desconectar

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket para o server
server.bind(ADDR) # Associa o socket ao ip e porta

# Função designada à thread para gerenciar o client
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected: # Loop de conexão ativa
        msg_length = conn.recv(HEADER).decode(FORMAT) # Recebe o tamanho da mensagem em 64 bytes
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT) # Recebe a mensagem do client

            if msg == DISCONNECT_MSG: # Verifica mensagem de desconexão
                connected = False 
            
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT)) # Envia confirmação de recebimento pro client
        
    conn.close() # Encerra a conexão 

def start():
    server.listen() # Inicia o servidor para receber requisições
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr)) # Cria thread designada a gerenciar uma nova conexão
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}") # Print do número de conexões ativas

print("[STARTING] server is starting...")
start()