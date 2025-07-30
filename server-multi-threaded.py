import socket
import threading

server_port= 5000
hostname = socket.gethostname()
server_ip = socket.gethostbyname(hostname)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, server_port))
server.listen(5)

def handle_client(client_socket, addr):
    print(f"Connection established with {addr}")
    connected = True
    
    while connected:
        message = client_socket.recv(1024).decode("utf-8")
        if not message:
            connected = False
            break
        print(f"Received message: {message}")
        response = "Message received"
        client_socket.send(response.encode("utf-8"))
        
    client_socket.close()

while True:
    client_socket, addr = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()
    