#! /usr/bin/env python
import socket


def receive(sock, msglen):
    msg = ""
    while len(msg) < msglen:
        chunk = sock.recv(msglen - len(msg))
        print(repr(chunk))
        if chunk == "":
            print("chao")
            raise RuntimeError("broken")
        if chunk in ["close", "close\n", "close\r\n"]:
            print(repr(chunk))
            sock.close()
            break
        msg = msg + chunk
        print(repr(msg))

    return msg


def send(sock, msg):
    total_sent = 0
    while total_sent < len(msg):
        sent = sock.send(msg[total_sent:])
        print(sent)
        if sent == 0:
            print("chao cacao")
            raise RuntimeError("broken")
        total_sent = total_sent + sent


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 2223))
    server_socket.listen(1)
    while True:
        client_socket, remote_address = server_socket.accept()
        while True:
            data = receive(client_socket, 1024)
            if data == "close":
                client_socket.close()
                break
            send(client_socket, data.upper())



def server2():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 2222))
    server_socket.listen(1)
    while True:
        client_socket, remote_address = server_socket.accept()
        while True:
            data = client_socket.recv(1024)
            if data in ["close", "close\n", "close\r\n"]:
                client_socket.close()
                break
            client_socket.send(data)

server2()

# server()
