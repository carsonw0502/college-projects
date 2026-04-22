import socket
import threading

# Flag to stop the program and close client/server individually
stop = threading.Event()

# Receive message from server
def message_receive(client_socket):
    while not stop.is_set():
        try:
            client_socket.settimeout(1.0)
            msg = client_socket.recv(1024).decode()
            if not msg:
                print("Server disconnected")
                stop.set()
                break
            print(f"\nServer: {msg}")

            # Print prompt again
            print(f"Enter message: ", flush=True)

        except socket.timeout:
            continue
        except:
            break

# Send message to server
def message_send(client_socket):
    while not stop.is_set():
        try:
            msg = input("Enter message: ")

            # Close the connection if the message is 'end'
            if msg.lower() == 'end':
                print("Closing connection...")
                stop.set()
                break

            # If the message isn't 'end', send to server
            client_socket.send(msg.encode())

        except:
            break


# Start client
def start_client():

    # Create socket, host and port
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 8000

    try:

        # Connect to server
        client_socket.connect((host, port))
        print(f"Connected to {host}:{port}")
        print("Type 'end' to exit\n")

        # Create threads to send and receive messages in parallel
        receive_thread = threading.Thread(target=message_receive, args=(client_socket,))
        send_thread = threading.Thread(target=message_send, args=(client_socket,))

        # Start each thread
        receive_thread.start()
        send_thread.start()

        # Wait for threads to finish before closing connection
        receive_thread.join()
        send_thread.join()

        # Close connection
        client_socket.close()
        print("Connection closed")

    except ConnectionRefusedError:
        print("Failed to connect. Ensure server program is running")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Connection closed")

# Start client
start_client()