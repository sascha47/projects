import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('10.11.2.6', 12345))  # IP address of Ubuntu

message_to_server = "Hello Hal, this is the client!"

client_socket.send(message_to_server.encode())

response_from_server = client_socket.recv(1024).decode()

print(f"Message from server: {response_from_server}")

client_socket.close()
