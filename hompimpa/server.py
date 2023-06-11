import socket # Import socket module
import threading # Import threading module
import random # Import random module

def handle_client(clientsocket, addr, room_code):
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
        while len(choices) < len(rooms[room_code]):
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
# Listen for up to 4 client connections
s.listen(4)

# A global list to store the choices and the client sockets
choices = []

# A global dictionary to store the room codes and the clients in each room
rooms = {}

while True:
    # Accept a new client connection
    c, addr = s.accept()
    print("Got connection from", addr)

    # Send a welcome message to the client 
    c.send(b"Welcome to Hompimpa!")

    # Ask the client to enter a room code or create a new one
    c.send(b"Please enter a room code or type 'new' to create a new room")

    # Receive the room code from the client (changed variable name from 'code' to 'room_code')
    room_code = c.recv(1024).decode()

    # Check if the client wants to create a new room
    if room_code == "new":
        print("Creating a new room...")
        # Generate a random four-digit room code
        room_code = str(random.randint(1000, 9999))

        # Send the room code to the client
        print("Sending the room code to the client...")
        c.send(("Your room code is: " + room_code).encode())
        
        # Create a new entry in the rooms dictionary with the room code as the key and an empty list as the value
        rooms[room_code] = []

        # Append the client socket to the list of clients in that room
        rooms[room_code].append(c)

    else:
        # Check if the room code exists in the rooms dictionary (changed variable name from 'code' to 'room_code')
        if room_code in rooms:
            # Append the client socket to the list of clients in that room
            rooms[room_code].append(c)
            # Send a message to the client that they have joined the room (changed variable name from 'code' to 'room_code')
            c.send(("You have joined room " + room_code).encode())
        else:
            # Send an error message to the client
            c.send(b"Invalid room code")

            # Close the connection
            c.close()
            
            # Continue to accept another connection (added this line)
            continue

    # Start a new thread to handle the client connection
    t = threading.Thread(target=handle_client, args=(c, addr, room_code))
    t.start()
