import tkinter as tk
from tkinter import ttk
import pickle
import subprocess
import random
from PIL import Image, ImageTk
import platform
import threading
import time

from room import room

class waiting(tk.Frame):
    def __init__(root, master, menu_manager, room_code):
        super().__init__(master)
        root.menu_manager = menu_manager
        root.room_code = tk.StringVar(value=room_code)
        root.list_player = tk.StringVar()
        root.load_image()
        root.create_canvas()
        root.create_widgets()
        root.start_player_count_update()
        root.game_started = False
    
    def load_image(root):
        root.background_image = Image.open('aset/waiting.png')
        if platform.system() == "Windows":
            import ctypes
            user32 = ctypes.windll.user32
            root.screen_width = user32.GetSystemMetrics(0)
            root.screen_height = user32.GetSystemMetrics(1)
        else:
            root.screen_width = 1400
            root.screen_height = 882

        root.background_image = root.background_image.resize((root.screen_width, root.screen_height), Image.ANTIALIAS)
        root.background_photo = ImageTk.PhotoImage(root.background_image)

    def create_canvas(root):
        root.background_canvas = tk.Canvas(root, width=root.screen_width, height=root.screen_height)
        root.background_canvas.pack()
        root.background_canvas.create_image(0, 0, anchor=tk.NW, image=root.background_photo)

    def create_widgets(self):
        room_label = ttk.Label(self.background_canvas, text="ID Room", font=("Arial", 32),  foreground="blue", background="")
        room_label.place(x=self.screen_width // 2, y=self.screen_height // 4, anchor=tk.CENTER)

        room_code_label = ttk.Label(self.background_canvas, textvariable=self.room_code, font=("Arial", 20, "bold"),  foreground="blue", background="")
        room_code_label.place(x=self.screen_width // 2, y=self.screen_height // 4 + 40, anchor=tk.CENTER)

        room_label = ttk.Label(self.background_canvas, text="Send the code to play with others!", font=("Arial", 16),  foreground="blue", background="")
        room_label.place(x=self.screen_width // 2, y=self.screen_height // 4 + 80, anchor=tk.CENTER)

        player_count_label = ttk.Label(self.background_canvas, textvariable=self.list_player, font=("Arial", 16, "bold"), foreground="blue", background="")
        player_count_label.place(x=self.screen_width // 2, y=self.screen_height // 4 + 120, anchor=tk.CENTER)

    # def count_player(root):
    #     send_data = {
    #         'command' : "GET DETAIL ROOM",
    #         'id_room' : root.menu_manager.id_room,
    #         'name'    : root.menu_manager.name
    #     }

    #     root.menu_manager.socket.send(pickle.dumps(send_data))

    #     data = root.menu_manager.socket.recv(2048)
    #     data = pickle.loads(data)

    #     # count number of player from list_player
    #     player_count = len(data['list_player'])
    #     root.list_player.set(f"{player_count}/3 people joined")
    #     if player_count == 3:
    #         root.start_game()
    def start_player_count_update(root):
        player_count_thread = threading.Thread(target=root.update_player_count)
        player_count_thread.daemon = True 
        player_count_thread.start()

    def update_player_count(root):
        while True:
            send_data = {
                'command': "GET DETAIL ROOM",
                'id_room': root.menu_manager.id_room,
                'name': root.menu_manager.name
            }

            root.menu_manager.socket.send(pickle.dumps(send_data))

            data = root.menu_manager.socket.recv(2048)
            data = pickle.loads(data)

            player_count = len(data['list_player'])
            root.list_player.set(f"{player_count}/3 people has joined")

            if player_count == 3 and not root.game_started:
                root.game_started = True
                root.start_game()

            # Wait for a certain period before checking the player count again
            time.sleep(1)  # Adjust the sleep duration as needed


    def start_game(root):
        subprocess.call(["python3", "tampilan.py"])