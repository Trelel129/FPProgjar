import socket # Import socket module
import threading # Import threading module

def handle_client(clientsocket, addr):
    # This function will handle each client connection in a separate thread
    print(f"New connection from {addr}")
    while True:
        # Receive the choice from the client (up or down)
        choice = clientsocket.recv(1024).decode()
        if not choice:
            # If the client disconnects, break the loop
            break
        print(f"{addr} chose {choice}")
        # Add the choice and the client socket to a global list
        choices.append((choice, clientsocket))
        # Wait for all the clients to send their choices
        while len(choices) < num_clients:
            pass
        # Check the majority choice
        ups = sum(1 for c, _ in choices if c == "up")
        downs = sum(1 for c, _ in choices if c == "down")
        if ups > downs:
            majority = "up"
        elif downs > ups:
            majority = "down"
        else:
            majority = "tie"
        # Send the result to the client
        if choice == majority:
            result = "You are in"
        elif majority == "tie":
            result = "It's a tie"
        else:
            result = "You are out"
        clientsocket.send(result.encode())
        # Remove the choice and the client socket from the global list
        choices.remove((choice, clientsocket))
    # Close the connection
    clientsocket.close()
    print(f"Connection from {addr} closed")

# Create a socket object
s = socket.socket()
# Get local machine name
host = socket.gethostname()
# Reserve a port for your service
port = 50000

print("Server started!")
print("Waiting for clients...")

# Bind to the port
s.bind((host, port))
# Listen for up to 5 client connections
s.listen(5)

# A global list to store the choices and the client sockets
choices = []
# A global variable to store the number of clients
num_clients = 3

while True:
    # Accept a new client connection
    c, addr = s.accept()
    # Create a new thread to handle the client connection
    t = threading.Thread(target=handle_client, args=(c, addr))
    t.start()
