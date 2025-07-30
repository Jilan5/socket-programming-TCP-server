# Simple Socket Programming Tutorial

This tutorial shows how to use the provided server and client Python scripts for basic message exchange.

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

---

## **Notes**
- Make sure the server is running before starting the client.
- Use the correct IP address for your server in `client.py` if connecting remotely.
- Open port 5000 on your server