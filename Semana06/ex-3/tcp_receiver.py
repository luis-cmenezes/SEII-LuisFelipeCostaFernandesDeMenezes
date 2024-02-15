import socket

TCP_IP = "127.0.0.1" # Define o endereço IP do servidor TCP
FILE_PORT = 5005 # Define a porta para o envio do nome do arquivo
DATA_PORT = 5006 # Define a porta para envio dos dados do arquivo
buf = 1024 # Tamanho do buffer para leitura de dados do socket


sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um socket para conexões do nome do arquivo
sock_f.bind((TCP_IP, FILE_PORT)) # Liga o socket ao IP e porta de nome do arquivo
sock_f.listen(1) # Permite conexões

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um socket para conexões dos dados do arquivo
sock_d.bind((TCP_IP, DATA_PORT)) # Liga o socket ao IP e porta de dados do arquivo
sock_d.listen(1) # Permite conexões


while True:
    conn, addr = sock_f.accept() # Aceita conexão no socket de envio do nome do arquivo
    data = conn.recv(buf) # Recebe os dados da conexão
    if data:
        print(f"File name: {data}") # Printa o nome recebido
        file_name = data.strip() # Remove espaços em branco do nome recebido

    f = open(file_name, 'wb') # Escreve no arquivo em modo binário

    conn, addr = sock_d.accept() # Aceita conexão no socket de envio dos dados do arquivo
    while True:
        data = conn.recv(buf) # Recebe os dados do sender
        if not data: # Encerra o recebimento caso não haja mais nada
            break 
        f.write(data) # Escreve o que foi recebido no arquivo

    print (f"Finish! {file_name}") # Indica a finalização do procedimento
    f.close() # Fecha o arquivo