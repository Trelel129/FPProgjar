import tkinter as tk
from tkinter import ttk
import pickle
import subprocess

from room import room
import random

class waiting(tk.Frame):
    def __init__(root, master, menu_manager):
        super().__init__(master)
        root.menu_manager = menu_manager

        root.room_code = tk.StringVar()
        root.player_list = tk.StringVar()
        
        root.create_widgets()

    def create_widgets(root):
        send_data = {
            'command' : "GET DETAIL ROOM",
            'room_id' : root.menu_manager.room_id,
            'name'    : root.menu_manager.name
        }

        root.menu_manager.socket.send(pickle.dumps(send_data))
        print(f'Send data to server: {send_data}')

        data = root.menu_manager.socket.recv(2048)
        data = pickle.loads(data)

        print(data)

        room_code_label = ttk.Label(root, text='Room Code: ')
        room_code_label.pack()

        room_code_value = ttk.Label(root, text=root.menu_manager.room_id)
        room_code_value.pack()
        
        num_player_label = ttk.Label(root, text="Number of Players:")
        num_player_label.pack()

        num_player_value = ttk.Label(root, text=data['num_players'])
        num_player_value.pack()

        player_list_label = ttk.Label(root, text="Player List:")
        player_list_label.pack()

        player_string = '\n'.join(data['player_list'])
        player_list_value = ttk.Label(root, text=player_string)
        player_list_value.pack()

        start_button = ttk.Button(root, text="Start", command=root.start_game)
        start_button.pack()

    def show_sog(root):
        root.menu_manager.show_menu("sog")

    def start_game(root):
        subprocess.call(["python3", "tampilan.py"])

        data = root.menu_manager.socket.recv(2048)
        data = pickle.loads(data)

        player_string = '\n'.join('player_list')
        root.player_list_value.configure(text=player_string)