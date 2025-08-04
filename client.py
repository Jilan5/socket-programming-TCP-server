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
    
while True: 
    user_input = input("Enter a message to send to the server (or 'exit' to quit): ")
    send_message(user_input)
    if user_input.lower() == 'exit':
        print("Exiting client.")
        break
