import socket

format = "utf-8"
server_port= 5000
hostname = socket.gethostname()
server_ip = socket.gethostbyname(hostname)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

def send_message(message):

    client.send(message.encode(format))
    response = client.recv(1024).decode(format)
    print(f"Server response: {response}")
    

send_message("Hello from the client!")
client.close()