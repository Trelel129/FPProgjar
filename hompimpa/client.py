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

msg = s.recv(1024).decode() 
print(msg)
msg = s.recv(1024).decode() 
print(msg)

code = input()
s.send(code.encode())
msg = s.recv(1024).decode() 
print(msg)
if msg != "Invalid room code. Please try again":
    while True:
        choice = input("Enter your choice (up or down) or type 'quit' to exit: ")
        if choice == "quit":
            s.close()
            break
        else:
            s.send(choice.encode())
            result = s.recv(1024).decode()
            print(f"The result is: {result}")

s.close()
