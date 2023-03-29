import socket

master = socket.socket()

host = "0.0.0.0"

port = 8920

master.bind((host, port))

master.listen(1)

slave, address = master.accept()

while True:
    print(">", end=" ")
    command = input()

    slave.send(command.encode())

    if command == "exit":
        break

    output = slave.recv(5000)
    print(output.decode())

master.close()