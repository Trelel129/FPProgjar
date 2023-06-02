# Client side
import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service
port = 12345

# Connect to the server
s.connect((host, port))

# Receive a welcome message from the server
print(s.recv(1024).decode())

# Define moves
moves = ["batu", "kertas", "gunting"]

# Start the game loop
while True:
    # Choose a move from the moves list
    client_move = input("Choose your move: ")

    # Check if the client wants to quit
    if client_move == "quit":
        break

    # Send the client's move to the server
    s.send(client_move.encode())

    # Receive the other player's move and the outcome from the server
    data = s.recv(1024).decode()

    # Check if the data is empty, which means the server has closed the connection
    if not data:
        break

    # Print the data
    print(data)

# Close the socket
s.close()