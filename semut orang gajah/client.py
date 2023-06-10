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
msg = s.recv(1024).decode() 
print(msg)

# Receive the prompt to enter a room code or create a new one
msg = s.recv(1024).decode() 
print(msg)

# Enter the room code or type ‘new’
code = input()

# Send the room code to the server
s.send(code.encode())

# Receive the confirmation or error message from the server
msg = s.recv(1024).decode() 
print(msg)

if msg != "Invalid room code. Please try again":
    # Start the game loop
    while True:
        # Enter your move or type ‘quit’ to exit
        move = input("Enter your move (semut, orang, gajah) or type ‘quit’ to exit: ")

        # Send your move to the server
        s.send(move.encode())

        # Check if you want to quit
        if move == "quit":
            # Close the connection
            s.close()
            break

        # Receive the result of the game from the server
        msg = s.recv(1024).decode()
        print(msg)

        # Check if the game is over
        if msg == "Game over!":
            # Close the connection
            s.close()
            break

# Close the connection
s.close()
