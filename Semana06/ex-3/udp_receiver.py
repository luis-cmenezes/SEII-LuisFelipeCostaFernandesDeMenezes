import socket # Módulo de comunicação de rede
import select # Módulo para monitoramento de descritores de arquivo

UDP_IP = "127.0.0.1" # Define o endereço IP do servidor UDP
IN_PORT = 5005 # Define a porta do servidor UDP
timeout = 3 # Define o tempo limite para aguardar por dados em segundos


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria um socket para UDP
sock.bind((UDP_IP, IN_PORT)) # Liga o soquete ao endereço IP e à porta especificada

while True: # Recebe dados continuamente
    data, addr = sock.recvfrom(1024) # Recebe dados do client
    if data: # Verifica se recebeu dados
        print(f"File name: {data}") # Indica o nome do arquivo recebido
        file_name = data.strip() # Remove espaços em branco do nome recebido

    f = open(file_name, 'wb') # Escreve no arquivo em modo binário

    while True: # Recebe os dados do arquivo
        ready = select.select([sock], [], [], timeout) # Verifica se há dados disponíveis para leitura
        if ready[0]: # Se ainda houverem dados à receber
            data, addr = sock.recvfrom(1024) # Recebe dados do arquivo do cliente UDP
            f.write(data) # Escreve os dados recebidos no arquivo
        else: # Se não houver mais dados à receber
            print(f"%s Finish! {file_name}") # Indica finalização do recebimento
            f.close() # Fecha o arquivo
            break