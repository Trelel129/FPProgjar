import select
import socket
import sys
import threading
import pickle

client_sockets = []
rooms = {}
players = {}

class Server:
    def __init__(root):
        root.threads = []
        root.host = 'localhost'
        root.port = 9000
        root.backlog = 4
        root.size = 1024
        root.server = None
        
    def open_socket(root):
        root.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        root.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        root.server.bind((root.host,root.port))
        root.server.listen(5)

    def run(root):
        root.open_socket()
        input = [root.server]
        running = 1
        while running:
            inputready,outputready,exceptready = select.select(input,[],[])
            for s in inputready:
                if s == root.server:
                    client_socket, client_address = root.server.accept()
                    print(f"{client_address} connected to server")
                    client_sockets.append(client_socket)
                    c = Client(client_socket, client_address)
                    c.start()
                    root.threads.append(c)
                elif s == sys.stdin:
                    junk = sys.stdin.readline()
                    running = 0

        root.server.close()
        for c in root.threads:
            c.join()

class Client(threading.Thread):
    def __init__(root, client, address):
        threading.Thread.__init__(root)
        root.client = client
        root.address = address
        root.size = 1024

    def run(root):
        running = 1
        print(client_sockets)
        print(f'address: {root.address}')

        while running:
            data = root.client.recv(root.size)
            data = pickle.loads(data)
 
            if (data['command'] == "CREATE ROOM"):
                id_room = data['id_room']
                rooms[id_room] = {"num_players": [], "list_player": []}
                rooms[id_room]["list_player"].append(data['name'])
                rooms[id_room]["num_players"].append(data['players'])
                print(f'{data["name"]} CREATE ROOM with room id: {id_room}')

            if (data['command'] == "JOIN ROOM"):
                id_room = data['id_room']
                if id_room in rooms:
                    rooms[id_room]["list_player"].append(data['name'])
                    print(f'{data["name"]} JOIN ROOM with id: {id_room}')

            if (data['command'] == "GET DETAIL ROOM"):
                send_data = rooms[data['id_room']]
                print(f'{data["name"]} GET DETAIL ROOM: {send_data}')
                root.client.send(pickle.dumps(send_data))
            
            if data['command'] == "CHECK ROOM":
                id_room = data['id_room']
                
                send_data = {
                    'status' : ''
                }

                if id_room in rooms:
                    send_data['status'] = 'EXIST'
                else:
                    send_data['status'] = 'DOES NOT EXIST'

                root.client.send(pickle.dumps(send_data))
            
            if (data['command'] == "CHECK ROOM ID"):
                send_data = {
                    'status' : ''
                }

                if data['id_room'] in rooms:
                    send_data['status'] = 'ROOM ID EXIST'
                else:
                    send_data['status'] = 'ROOM ID DOES NOT EXIST'
                
                root.client.send(pickle.dumps(send_data))


if __name__ == "__main__":
    s = Server()
    s.run()