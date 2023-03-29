import socket

HOST = "localhost"
PORT = 8010

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello World")
    data = s.recv(1024)

print(f"Recieved {data!r}")
