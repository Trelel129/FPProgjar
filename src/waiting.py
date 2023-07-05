import tkinter as tk
from tkinter import ttk
import pickle
import subprocess
import random

from room import room

class waiting(tk.Frame):
    def __init__(root, master, menu_manager):
        super().__init__(master)
        root.menu_manager = menu_manager

        root.room_code = tk.StringVar()
        root.list_player = tk.StringVar()
        
        root.count_player()
    
    def count_player(root):
        send_data = {
            'command' : "GET DETAIL ROOM",
            'id_room' : root.menu_manager.id_room,
            'name'    : root.menu_manager.name
        }

        root.menu_manager.socket.send(pickle.dumps(send_data))

        data = root.menu_manager.socket.recv(2048)
        data = pickle.loads(data)

        # count number of player from list_player
        player_count = len(data['list_player'])
        if player_count == 2:
            root.start_game()

    def start_game(root):
        subprocess.call(["python3", "tampilan.py"])