import socket # Import socket module

# Create a socket object
s = socket.socket()
# Get local machine name
host = socket.gethostname()
# Reserve a port for your service
port = 50000

# Connect to the server
s.connect((host, port))
print("Connected to the server!")

while True:
    # Ask the user to enter their choice (up or down)
    choice = input("Enter your choice (up or down): ")
    # Send the choice to the server
    s.send(choice.encode())
    # Receive the result from the server
    result = s.recv(1024).decode()
    print(f"The result is: {result}")