import os
import sys
import socket

# print(os.getpid())
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 2222))
server_socket.listen(10)
while True:
    client_socket, remote_address = server_socket.accept()
    child_pid = os.fork()
    if child_pid == 0:
        while True:
            data = client_socket.recv(1024)
            if not data:
                client_socket.close()
                sys.exit()
            if data in [b"close", b"close\n", b"close\r\n"]:
                # print(repr(data), os.getpid())
                client_socket.close()
                sys.exit()
            # data = str(os.getpid()) + ": " + str(data)
            client_socket.send(data.encode())

    else:
        client_socket.close()