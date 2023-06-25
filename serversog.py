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

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = s.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(32)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
