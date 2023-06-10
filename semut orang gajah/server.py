# Server side
import socket
import random

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service
port = 12345

# Bind to the port
s.bind((host, port))

# Start listening for connections
s.listen(5)

# Define moves
moves = ["semut", "orang", "gajah"]

# Define outcomes
outcomes = {
    ("semut", "semut"): "draw",
    ("semut", "orang"): "anda kalah",
    ("semut", "gajah"): "anda menang",
    ("orang", "semut"): "anda menang",
    ("orang", "orang"): "draw",
    ("orang", "gajah"): "anda kalah",
    ("gajah", "semut"): "anda kalah",
    ("gajah", "orang"): "anda menang",
    ("gajah", "gajah"): "draw"
}

# Create a list to store the connected clients and their moves
clients = []

# Accept two connections from the clients
for i in range(2):
    # Accept a connection from a client
    c, addr = s.accept()
    print("Got connection from", addr)

    # Send a welcome message to the client
    c.send(("Welcome to gajah semut orang! You are player " + str(i+1)).encode())

    # Append the client and its move to the list
    clients.append([c, None])

# Start the game loop
while True:
    # Loop through each client
    for i in range(2):
        # Get the client and its move from the list
        c, move = clients[i]

        # Try to receive the client's move
        try:
            move = c.recv(1024).decode()
        except:
            # If an error occurs, assume the client has disconnected
            print("Player", i+1, "has disconnected")
            move = "quit"

        # Check if the client wants to quit
        if move == "quit":
            # Send a goodbye message to the client
            c.send(b"Goodbye!")

            # Close the connection
            c.close()

            # Remove the client from the list
            clients.pop(i)

            # Break out of the loop
            break

        # Update the client's move in the list
        clients[i][1] = move

    # Check if there are still two clients in the list
    if len(clients) == 2:
        # Get the moves of both clients
        move1 = clients[0][1]
        move2 = clients[1][1]

        # Check if both clients are ready
        if move1 and move2:
            # Compare the moves and get the outcome for player 1
            outcome1 = outcomes[(move1, move2)]

            # Get the opposite outcome for player 2
            if outcome1 == "draw":
                outcome2 = outcome1
            elif outcome1 == "anda menang":
                outcome2 = "anda kalah"
            else:
                outcome2 = "anda menang"

            # Send the moves and outcomes to both clients
            clients[0][0].send((move2 + "\n" + outcome1).encode())
            clients[1][0].send((move1 + "\n" + outcome2).encode())

            # Reset the moves of both clients in the list
            clients[0][1] = None
            clients[1][1] = None

    else:
        # If there is only one client left in the list, send a message that the other player has left
        c = clients[0][0]
        c.send(b"The other player has left the game")

        # Close the connection
        c.close()

        # Break out of the loop
        break