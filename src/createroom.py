import tkinter as tk
from tkinter import ttk
import pickle
import random
import platform
from PIL import Image, ImageTk
from waiting import waiting

class CustomEntry(tk.Frame):
    def __init__(root, master, style=None, **kwargs):
        super().__init__(master, **kwargs)
        root.style = style
        root.create_widgets()

    def create_widgets(root):
        root.entry_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
        root.entry_frame.pack(fill=tk.BOTH, expand=True)
        root.entry_frame.bind("<Button-1>", lambda event: root.focus_set())
        root.entry_label = ttk.Label(root.entry_frame, style=root.style)
        root.entry_label.pack(fill=tk.BOTH, expand=True)

    def get(root):
        return root.entry_label.cget("text")

    def config(root, **kwargs):
        root.entry_label.config(**kwargs)

    def insert(root, index, string):
        root.entry_label.config(text=root.entry_label.cget("text") + string)

    def delete(root, start, end=None):
        text = root.entry_label.cget("text")
        if end is None:
            root.entry_label.config(text=text[:start])
        else:
            root.entry_label.config(text=text[:start] + text[end:])


class createroom(tk.Frame):
    def __init__(root, master, menu_manager):
        super().__init__(master)
        root.menu_manager = menu_manager
        root.load_image()
        root.create_canvas()
        # root.create_widgets()

    def load_image(root):
        root.background_image = Image.open('aset/bg.png')
        root.modal_create_room_image = Image.open('aset/button.png')
        root.name_input_image = Image.open('aset/Name.png')
        root.create_room_btn_image = Image.open('aset/create room.png')
        root.input_name_image = Image.open('aset/input.png')
        root.back_btn_image = Image.open('aset/back.png')

        # ukuran layar
        if platform.system() == "Windows":
            import ctypes
            user32 = ctypes.windll.user32
            root.screen_width = user32.GetSystemMetrics(0)
            root.screen_height = user32.GetSystemMetrics(1)
        else:
            root.screen_width = 1400
            root.screen_height = 882

        root.background_image = root.background_image.resize(
            (root.screen_width, root.screen_height), Image.ANTIALIAS)
        root.modal_create_room_image = root.modal_create_room_image.resize(
            (int(root.screen_width*0.4), int(root.screen_height*0.8)), Image.ANTIALIAS)
        root.name_input_image = root.name_input_image.resize(
            (int(root.screen_width / 15), int(root.screen_height / 24)), Image.ANTIALIAS)
        root.create_room_btn_image = root.create_room_btn_image.resize(
            (int(root.screen_width / 10), int(root.screen_height / 16)), Image.ANTIALIAS)
        root.input_name_image = root.input_name_image.resize(
            (int(root.screen_width / 5), int(root.screen_height / 10)), Image.ANTIALIAS)
        root.back_btn_image = root.back_btn_image.resize(
            (int(root.screen_width / 10), int(root.screen_height / 16)), Image.ANTIALIAS)

        root.background_photo = ImageTk.PhotoImage(root.background_image)
        root.modal_create_room_photo = ImageTk.PhotoImage(root.modal_create_room_image)
        root.name_input_photo = ImageTk.PhotoImage(root.name_input_image)
        root.create_room_btn_photo = ImageTk.PhotoImage(root.create_room_btn_image)
        root.input_name_photo = ImageTk.PhotoImage(root.input_name_image)
        root.back_btn_photo = ImageTk.PhotoImage(root.back_btn_image)

    def create_canvas(root):
        root.background_canvas = tk.Canvas(
            root, width=root.screen_width, height=root.screen_height)
        root.background_canvas.pack()
        root.background_canvas.create_image(
            0, 0, anchor=tk.NW, image=root.background_photo)
        root.background_canvas.create_image(int(root.screen_width * 0.3), int(
            root.screen_height / 12), anchor=tk.NW, image=root.modal_create_room_photo)
        root.background_canvas.create_image(int(root.screen_width * 0.475), int(
            root.screen_height / 5), anchor=tk.NW, image=root.name_input_photo)

        root.name_entry = ttk.Entry(root.background_canvas)
        root.name_entry.place(x=int(root.screen_width * 0.46), y=int(root.screen_height / 4))

        create_button = ttk.Button(
            root.background_canvas, image=root.create_room_btn_photo, command=root.create_room)
        create_button.place(x=int(root.screen_width * 0.45), y=int(root.screen_height * 0.6))

        create_button = ttk.Button(
            root.background_canvas, image=root.back_btn_photo, command=root.menu_manager.show_main_menu)
        create_button.place(x=int(root.screen_width * 0.45), y=int(root.screen_height * 0.7))

    def create_widgets(root):
        name_label = ttk.Label(root, text="Choose Username:")
        name_label.pack()
        root.name_entry = CustomEntry(root, style="Custom.TEntry")
        root.name_entry.pack()
        create_button = ttk.Button(root, text="Create Room", command=root.create_room)
        create_button.pack()
        back_button = ttk.Button(root, text="Back to Menu", command=root.menu_manager.show_main_menu)
        back_button.pack()

    def create_room(root):
        name = root.name_entry.get()
        players = 4
        root.menu_manager.name = name
        print(f'Set player name to: {root.menu_manager.name}')
        id_room_check = True
        while id_room_check:
            id_room = "".join(str(random.randint(0, 9)) for _ in range(6))
            root.menu_manager.id_room = id_room
            print(f'Set room id to: {root.menu_manager.id_room}')
            send_data = {
                'command' : "CHECK ROOM ID",
                'id_room' : id_room,
                'name': name
            }

            root.menu_manager.socket.send(pickle.dumps(send_data))
            print(f'Send data to server: {send_data}')
            data = root.menu_manager.socket.recv(2048)
            data = pickle.loads(data)
            if data['status'] == 'ROOM ID DOES NOT EXIST':
                id_room_check = False

        send_data = {
            'command': "CREATE ROOM",
            'id_room': id_room,
            'name': name,
            'players': players
        }

        root.menu_manager.socket.send(pickle.dumps(send_data))
        print(f'Send data to server: {send_data}')

        root.menu_manager.menus["waiting_room"] = waiting(
            root.menu_manager, root.menu_manager)
        root.menu_manager.show_menu("waiting_room")
