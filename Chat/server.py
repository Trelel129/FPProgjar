import atexit
import socket
import threading

def connectionThread(sock):
    while True:
        try:
            client, address = sock.accept()
        except:
            print("Something went wrong while accepting incoming connections!")
            break
        print("{} has connected.".format(address[0]))
        addresses[client] = address
        threading.Thread(target=clientThread, args=(client,)).start()

def clientThread(client):
    address = addresses[client][0]
    try:
        user = getNickname(client)
    except:
        print("Something went wrong while setting the nickname for {}!".format(address))
        del addresses[client]
        client.close()
        return
    print("{} set its nickname to {}!".format(address, user))
    users[client] = user
    try:
        client.send("Hi {}!".format(user).encode("utf8"))
    except:
        print("Communication error with {} ({}).".format(address, user))
        del addresses[client]
        del users[client]
        client.close()
        return
    broadcast("{} has joined the chat room!".format(user))

    while True:
        try:
            message = client.recv(2048).decode("utf8")
            print("{} ({}): {}".format(address, user, message))
            broadcast(message, user)
        except:
            print("{} ({}) has left.".format(address, user))
            del addresses[client]
            del users[client]
            client.close()
            broadcast("{} has left the chat.".format(user))
            break

def getNickname(client):
    client.send("Please type your nickname:".encode("utf8"))
    nickname = client.recv(2048).decode("utf8")
    alreadyTaken = False
    if nickname in users.values():
        alreadyTaken = True
        while alreadyTaken:
            client.send("This nickname has already been taken. Please choose a different one:".encode("utf8"))
            nickname = client.recv(2048).decode("utf8")
            if nickname not in users.values():
                alreadyTaken = False
    return nickname

def broadcast(message, sentBy = ""):
    try:
        if sentBy == "":
            for user in users:
                user.send(message.encode("utf8"))
        else:
            for user in users:
                user.send("{}: {}".format(sentBy, message).encode("utf8"))
    except:
        print("Something went wrong while broadcasting a message!")

def cleanup():
    if len(addresses) != 0:
        for sock in addresses.keys():
            sock.close()
    print("Cleanup done.")

def main():
    atexit.register(cleanup)
    host = ""
    port = 25001
    socketFamily = socket.AF_INET
    socketType = socket.SOCK_STREAM
    serverSocket = socket.socket(socketFamily, socketType)

    serverSocket.bind((host, port))
    serverSocket.listen()
    
    print("pyChat server is up and running!")
    print("Listening for new connections on port {}.".format(port))

    connThread = threading.Thread(target=connectionThread, args=(serverSocket,))
    connThread.start()
    connThread.join()
    
    cleanup()
    
    serverSocket.close()
    print("Server has shut down.")

users = {}
addresses = {}

if __name__ == "__main__":
    main()
    pass