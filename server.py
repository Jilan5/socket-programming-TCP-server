import socket

server_port= 5000
hostname = socket.gethostname()
server_ip = socket.gethostbyname(hostname)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, server_port))
server.listen(5)
print(f"Server listening on {server_ip}:{server_port}")

while True:
    client_socket, addr = server.accept()
    print(f"Connection established with {addr}")
    connected = True
    
    while connected:
        
        message = client_socket.recv(1024).decode("utf-8")
        if not message:
            connected = False

        print(f"Received message: {message}")
        response = "Message received"
        client_socket.send(response.encode("utf-8"))
    print(f"Client {addr} has disconnected.")
    client_socket.close()