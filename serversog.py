import socket
import random
import threading

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service
port = 12345

# Bind to the port
s.bind((host, port))

# Start listening for connections
s.listen(2)

# Define moves
moves = ["Semut", "Orang", "Gajah"]


# Define outcomes
outcomes = {
    ("Semut", "Semut"): "draw",
    ("Semut", "Orang"): "anda kalah",
    ("Semut", "Gajah"): "anda menang",
    ("Orang", "Semut"): "anda menang",
    ("Orang", "Orang"): "draw",
    ("Orang", "Gajah"): "anda kalah",
    ("Gajah", "Semut"): "anda kalah",
    ("Gajah", "Orang"): "anda menang",
    ("Gajah", "Gajah"): "draw"
}

# Create a dictionary to store the room codes and the clients in each room
rooms = {}

# Define a function to handle the game logic for each room
def game_room(code):
    # Get the list of clients in that room
    clients = rooms[code]


    # Start the game loop

    while True:
        # Loop through each client in that room
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

            # # Check if the client wants to quit
            # if move == "quit":
            #     # Send a goodbye message to the client
            #     c.send(b"Goodbye!")

            #     # Close the connection
            #     c.close()

            #     # Remove the client from the list of clients in that room
            #     clients.pop(i)

            #     # Break out of the loop
            #     break

            # Update the client's move in the list of clients in that room
            clients[i][1] = move

        # Check if there are still two clients in that room
        if len(clients) == 2:
            c.send(b"Start")
            # Get the moves of both clients in that room
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

                # Send the moves and outcomes to both clients in that room
                clients[0][0].send(("Anda: "+ move1 +"\nLawan: " + move2 + "\n" + outcome1).encode())
                clients[1][0].send(("Anda: "+ move2 +"\nLawan: " + move1 + "\n" + outcome2).encode())

                # Reset the moves of both clients in the list of clients in that room
                clients[0][1] = None
                clients[1][1] = None

        else:
            # If there is only one client left in that room, send a message that the other player has left
            c = clients[0][0]
            c.send(b"The other player has left the game")

            # Close the connection
            c.close()

            # Remove the room from the rooms dictionary
            rooms.pop(code)

            # Break out of the loop
            break

# Accept connections from the clients indefinitely
while True: 

    # Accept a connection from a client 
    c, addr = s.accept()
    print("Got connection from", addr)

    # Send a welcome message to the client
    c.send(b"Welcome to Gajah Semut Orang!")

    # Ask the client to enter a room code or create a new one
    c.send(b"Please enter a room code or type 'new' to create a new room")

    # Receive the client's input
    code = c.recv(1024).decode()

    # Check if the client wants to create a new room
    if code == "create":
        # Generate a random four-digit room code
        code = str(random.randint(1000, 9999))

        # Send the room code to the client
        c.send((code).encode())

        # Create a new entry in the rooms dictionary with the code as the key and an empty list as the value
        rooms[code] = []

        # Append the client and its move to the list of clients in that room
        rooms[code].append([c, None])

        # Create a new thread for that room and start it
        t = threading.Thread(target=game_room, args=(code,))
        t.start()

    else:
        # Check if the room code exists in the rooms dictionary
        if code in rooms:
            # Append the client and its move to the list of clients in that room
            rooms[code].append([c, None])

            # Send a message to the client that they have joined the room
            c.send(("You have joined room: " + code).encode())

            # Check if there are two clients in that room
            if len(rooms[code]) == 2:
                # Create a new thread for that room and start it
                t = threading.Thread(target=game_room, args=(code,))
                t.start()

        else:
            # Send an error message to the client that the room code is invalid
            c.send(b"Invalid room code. Please try again")

            # Close the connection
            c.close()