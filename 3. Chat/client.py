import socket

print("\nWelcome to Chat Room\n")
print("Initialising....\n")

PROTOCOL = 'utf-8'
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = input(str("Enter server address: "))
name = input(str("\nEnter your name: "))
port = 1233
print("\nTrying to connect to ", host, "(", port, ")\n")

s.connect((host, port))
print("Connected...\n")

s.send(name.encode(PROTOCOL))
s_name = s.recv(1024)
s_name = s_name.decode(PROTOCOL)
print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")

while True:
    message = s.recv(1024)
    message = message.decode(PROTOCOL)
    print(s_name, ":", message)
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat room!"
        s.send(message.encode(PROTOCOL))
        print("\n")
        break
    s.send(message.encode(PROTOCOL))