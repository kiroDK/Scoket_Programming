import socket

HOST = "localhost"
PORT = 8010

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, add = s.accept()
    with conn:
        print(f"connected by {add}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
