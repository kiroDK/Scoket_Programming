import socket

print("\nWelcome to Chat Room\n")
print("Initialising....\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1233
PROTOCOL = 'utf-8'

s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))

s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode(PROTOCOL)
print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
conn.send(name.encode(PROTOCOL))

while True:
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat room!"
        conn.send(message.encode(PROTOCOL))
        print("\n")
        break
    conn.send(message.encode(PROTOCOL))
    message = conn.recv(1024)
    message = message.decode(PROTOCOL)
    print(s_name,":",message)