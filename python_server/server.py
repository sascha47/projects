import socket



def start_server(server_ip, server_port):
    # Create a TCP/IP socket
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address
    server_sock.bind((server_ip, server_port))

    # Listen for incoming connections
    server_sock.listen(1)


    while True:
        # Wait for a connection
        print('Waiting for a connection...')
        client_socket, client_address = server_sock.accept()

        try:
            print('Connection from:', client_address)

            # Receive the data
            message_from_client = client_socket.recv(1024).decode()
            print(f"Message from client: {message_from_client}")

            response_to_client = "Hi client, I recieved your message!"
            client_socket.send(response_to_client.encode())

        finally:
            # Clean up the connection
            client_socket.close()

# Start the server
start_server('0.0.0.0', 12345) # Empty string for server_ip means listen on all available network interfaces
