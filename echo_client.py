#!/usr/bin/env python3
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_address = '198.162.52.47'
server_address = '10.0.2.15'
server_address = '0.0.0.0'
server_port = 1235
client_socket.connect((server_address, server_port))

message = 'Hello World'
print("Sending")
client_socket.send(message.encode())
response = client_socket.recv(1024).decode()
print("Test passed" if message == response else "Test failed")
