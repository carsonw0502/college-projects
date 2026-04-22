import socket
import threading

# List to store currently connected clients
clients = []
clients_lock = threading.Lock()


# Send messages to every client connected, but not the server
def broadcast(message, sender_socket):
    with clients_lock:
        for client_socket, _ in clients:
            if client_socket != sender_socket:
                try:
                    client_socket.send(message.encode())
                except:
                    pass

# Receive a message from a client and broadcast it to all others
def client_receive(client_socket, client_address):
    print(f"{client_address} connected (Total connections: {len(clients)})")
    try:
        while True:
            client_socket.settimeout(1.0)
            try:
                message = client_socket.recv(1024).decode()
            except socket.timeout:
                continue

            # Client connection closed
            if not message:
                break

            print(f"{client_address}: {message}")
            broadcast(f"{client_address}: {message}", client_socket)

    # Error checking, remove client from list and close the socket if an error is encountered
    except Exception as error:
        print(f"{client_address} has encountered an error: {error}")
    finally:
        with clients_lock:
            clients[:] = [(s, a) for s, a in clients if s is not client_socket]
        client_socket.close()
        print(f"{client_address} disconnected (Total connections: {len(clients)})")
        broadcast(f"{client_address} disconnected", client_socket)

# Start server
def start_server():

    # Create socket, host and port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "localhost"
    port = 8000

    # Reusable command, alleviates address in use errors when running multiple times
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Waiting for connection on {host}:{port}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()

            # Register client so broadcast can always pick it up
            with clients_lock:
                clients.append((client_socket, client_address))

            # Notify other clients that a new client connected
            broadcast(f"{client_address} connected", client_socket)

            # Create a thread for the client
            thread = threading.Thread(target=client_receive, args=(client_socket, client_address), daemon=True)
            thread.start()

    except KeyboardInterrupt:
        print("Shutting down server...")
    finally:
        with clients_lock:
            for client_socket, client_address in clients:
                client_socket.close()
        server_socket.close()
        print("Server closed")

# Run the server
start_server()
