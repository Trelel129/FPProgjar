import socket
import select

class Message:
    def __init__(self, text):
        self.text = text
        self.next = None

class MessageList:
    def __init__(self):
        self.head = None
    
    def add(self, text):
        newMessage = Message(text)
        if self.head is None:
            self.head = newMessage
        else:
            newMessage.next = self.head
            self.head = newMessage

class Client:
    def __init__(self, name, connection):
        self.name = name
        self.connection = connection
        self.next = None

class ClientList:
    def __init__(self):
        self.head = None
    
    def add(self, name, connection):
        newClient = Client(name, connection)
        if self.head is None:
            self.head = newClient
        
        else:
            newClient.next = self.head
            self.head = newClient
    
    def nameAvailable(self, name):
        client = self.head
        while client is not None:

            if client.name == name:
                return False
            client = client.next
        
        return True

    def getByConnection(self, connection):
        client = self.head
        while client is not None:
            if client.connection == connection:
                return client
            client = client.next
        return None

    def drop(self, client):
        temp = self.head
        if temp is None or client is None:
            return
        
        if temp == client:
            self.head = temp.next
            return
        
        while temp:
            if temp.next == client:
                temp.next = client.next
                return
            temp = temp.next

class Server:
    def __init__(self):
        self.host = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setblocking(0)
        self.socket.bind((self.host, 25013))
        self.port = self.socket.getsockname()[1]
        self.clientList = ClientList()

    def run(self):
        self.socket.listen()
        inputs = [self.socket]
        clientNumber = 0
        running = True
        while running:
            readable, writeable, exceptional = select.select(inputs, [], inputs, 0.1)
            messageBuffer = MessageList()
            for s in readable:
                if s is self.socket:
                    connection, client_address = s.accept()
                    connection.setblocking(0)
                    inputs.append(connection)
                    self.clientList.add(f"Client{clientNumber}", connection)
                    clientNumber += 1
                else:
                    message = s.recv(4096).decode()
                    if message:
                        print(f"Got message \"{message}\"\n")
                        if message.split(":")[0] == "name":
                            if self.clientList.nameAvailable(message.split(":")[1]):
                                client = self.clientList.getByConnection(s)
                                client.name = message.split(":")[1]
                                response = "available".encode()
                            else:
                                response = "taken".encode()
                            s.send(response)
                        elif message.split(":")[0] == "message":
                            splitMessage = message.split(":")
                            messageBuffer.add(f"message:{splitMessage[1]}:{splitMessage[2]}")
                            client = self.clientList.head
                            while client is not None:
                                if client.connection not in writeable:
                                    writeable.append(client.connection)
                                client = client.next
                    else:
                        exceptional.append(s)
            
            for s in writeable:
                messageEntry = messageBuffer.head
                message = ""
                while messageEntry is not None:
                    message += f"{messageEntry.text}\n"
                    messageEntry = messageEntry.next
                message = message.encode()
                if s is not self.socket:
                    s.send(message)

    def exit(self):
        pass

if __name__ == "__main__":
    server = Server()
    server.run()
    server.exit()