# Simple Socket Programming Tutorial
#
## Objective
- Demonstrate basic TCP socket programming in Python.
- Show how to build both single-threaded and multi-threaded servers.
- Enable interactive message exchange between client and server.
- Illustrate REPL-like command processing in network applications.
- Provide clear code examples and usage instructions.

This tutorial shows how to use the provided server and client Python scripts for basic message exchange.

---


## Key Code Components & REPL-like Command Processing

Before running the servers, let's briefly discuss the main parts of the code and how command processing works:

### Important Code Parts


**Client (`client.py`):**
```python
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

def send_message(message):
    client.send(message.encode("utf-8"))
    response = client.recv(1024).decode("utf-8")
    print(f"Server response: {response}")

while True:
    user_input = input("Enter a message to send to the server (or 'exit' to quit): ")
    send_message(user_input)
    if user_input.lower() == 'exit':
        print("Exiting client.")
        break
```
- Creates a TCP socket and connects to the server using the provided IP and port.
- Defines a `send_message` function to send user input to the server and print the response.
- Uses a `while True` loop to repeatedly prompt the user for input, send it to the server, and display the server's reply.
- Exits cleanly when the user types 'exit'.

**Single-Threaded Server (`server.py`):**
<img width="1388" height="851" alt="image" src="https://github.com/user-attachments/assets/226a33a8-2503-4860-98d4-09673d7d6cbe" />

```python
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, server_port))
server.listen(5)

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
```
- Sets up a TCP socket, binds to the IP and port, and listens for incoming connections.
- For each client, enters a loop to receive messages, print them, and send a response.
- Closes the connection when the client disconnects or sends no data.

**Multi-Threaded Server (`server-multi-threaded.py`):**
<img width="1303" height="795" alt="image" src="https://github.com/user-attachments/assets/09e42c41-f271-477f-928e-e795b46f5eb8" />

```python
import threading

def handle_client(client_socket, addr):
    print(f"Connection established with {addr}")
    connected = True
    while connected:
        message = client_socket.recv(1024).decode("utf-8")
        print(f"Received message from client {addr}: {message}")
        if message.lower() == 'exit':
            print(f"Client {addr} has disconnected.")
            connected = False
        response = "Message received"
        client_socket.send(response.encode("utf-8"))
    client_socket.close()

while True:
    client_socket, addr = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()
```
- Similar setup as the single-threaded server, but uses Python's `threading` module.
- Each client connection is handled in a separate thread, allowing multiple clients to interact with the server simultaneously.
- The `handle_client` function manages communication with each client.

### REPL-like Command Processing


- Both the client and server use a loop to process messages interactively, similar to a REPL (Read-Eval-Print Loop).
- The user can type commands, and the server responds immediately.
- Typing 'exit' as a command disconnects the client from the server and ends the session.

---

## 1. Single-Threaded Server & Client

### **Start the Server**
1. On your server/VM, run:
   ```bash
   python3 server.py
   ```

### **Run the Client**
1. On your local machine, edit `client.py`:
   - **If running both client and server on the same machine:**  
     No need to change `server_ip`; it will work as both are on the same machine.
   - **If connecting to a remote server:**  
     Set `server_ip` to your server's public IP.
2. Run:
   ```bash
   python3 client.py
   ```
3. The client will send a message and print the server's response.

#### 📸 Screenshot Example
<img width="1480" height="296" alt="image" src="https://github.com/user-attachments/assets/1be35a25-d2dd-4eda-a0b8-f0ac9f1c35da" />

<img width="1480" height="296" alt="image" src="https://github.com/user-attachments/assets/3fac0e6f-0e7f-47a7-8184-80ac0862dc72" />


---

## 2. Multi-Threaded Server & Client

### **Start the Multi-Threaded Server**
1. On your server/VM, run:
   ```bash
   python3 server-multi-threaded.py
   ```

### **Run Multiple Clients**
1. On any machine, edit `client.py`:
   - **If running locally:** No need to change `server_ip`.
   - **If connecting remotely:** Set `server_ip` to your server's public IP.
2. Run:
   ```bash
   python3 client.py
   ```
3. Multiple clients can connect and send messages at the same time.

#### 📸 Screenshot Example
<img width="1480" height="379" alt="image" src="https://github.com/user-attachments/assets/2fa27700-8e3e-4cb6-b10f-953e473a3d0f" />
<img width="1853" height="413" alt="image" src="https://github.com/user-attachments/assets/e12c7352-d9bf-42b8-8147-9529513a5daf" />




## What is Multithreading?

Multithreading is a programming technique that allows a program to run multiple threads (smaller units of a process) concurrently. Each thread can execute independently, sharing the same resources of the parent process. In the context of socket servers, multithreading enables the server to handle multiple client connections at the same time, with each client managed by a separate thread.

### How Multithreading Works in Python Socket Servers
- When a new client connects, the server creates a new thread dedicated to handling communication with that client.
- Each thread runs the same function (e.g., `handle_client`), allowing simultaneous message exchanges with multiple clients.
- Threads share the server's resources but operate independently, so one slow or disconnected client does not block others.
- Python's `threading` module makes it easy to create and manage threads.

**Example:**
```python
import threading

def handle_client(client_socket, addr):
    # Communicate with client
    pass

while True:
    client_socket, addr = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()
```

This approach is especially useful for chat servers, multiplayer games, or any application where many clients need to interact with the server at the same time.

## Pros and Cons: Single-Threaded vs Multi-Threaded Server

### Single-Threaded Server
**Pros:**
- Simple to implement and debug.
- Lower resource usage for very basic use cases.

**Cons:**
- Can only handle one client at a time; other clients must wait.
- Not suitable for real-world applications where multiple clients connect simultaneously.

### Multi-Threaded Server
**Pros:**
- Can handle multiple clients at the same time.
- More responsive and scalable for real-world scenarios.

**Cons:**
- More complex code (thread management, synchronization issues).
- Higher resource usage (each thread consumes memory and CPU).
- Potential for race conditions or deadlocks if not managed carefully.

## **Notes**
- Make sure the server is running before starting the client.
- Use the correct IP address for your server in `client.py` if connecting remotely.
- Open port 5000 on your server
