import socket


HOST = "127.0.0.1"
PORT = 30430

# Using resource management, we open a socket using AF_INET, which in turn uses IPv4 for our socket, and SOCK_STREAM uses TCP for our connection.
# We store these in the variable "s".

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    print("Waiting for a connection...\n")
    conn, addr = s.accept()


with conn:
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024) # The server will read up to 1kb of data from the client.
        if not data:
            break
        conn.sendall(data)

# The while loop repeats until the client sends an empty packet.

