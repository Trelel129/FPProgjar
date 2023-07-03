import tkinter as tk
from tkinter import ttk
import pickle
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
import platform

from waiting import waiting


class join(tk.Frame):
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
        root.room_code_image = Image.open('aset/Room Code.png')
        root.join_room_btn_image = Image.open('aset/join room.png')
        root.back_btn_image = Image.open('aset/back.png')

        # Get screen resolution
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
            (int(root.screen_width*0.4), int(root.screen_height*0.75)), Image.ANTIALIAS)
        root.name_input_image = root.name_input_image.resize(
            (int(root.screen_width / 15), int(root.screen_height / 24)), Image.ANTIALIAS)
        root.room_code_image = root.room_code_image.resize(
            (int(root.screen_width / 10), int(root.screen_height / 24)), Image.ANTIALIAS)
        root.join_room_btn_image = root.join_room_btn_image.resize(
            (int(root.screen_width / 10), int(root.screen_height / 16)), Image.ANTIALIAS)
        root.back_btn_image = root.back_btn_image.resize(
            (int(root.screen_width / 10), int(root.screen_height / 16)), Image.ANTIALIAS)

        # Convert images to Tkinter PhotoImage objects
        root.background_photo = ImageTk.PhotoImage(root.background_image)
        root.modal_create_room_photo = ImageTk.PhotoImage(root.modal_create_room_image)
        root.name_input_photo = ImageTk.PhotoImage(root.name_input_image)
        root.room_code_photo = ImageTk.PhotoImage(root.room_code_image)
        root.join_room_btn_photo = ImageTk.PhotoImage(root.join_room_btn_image)
        root.back_btn_photo = ImageTk.PhotoImage(root.back_btn_image)

    def create_canvas(root):
        root.background_canvas = tk.Canvas(root, width=root.screen_width, height=root.screen_height)
        root.background_canvas.pack()
        root.background_canvas.create_image(0, 0, anchor=tk.NW, image=root.background_photo)
        root.background_canvas.create_image(int(root.screen_width * 0.3), int(root.screen_height / 12), anchor=tk.NW, image=root.modal_create_room_photo)
        root.background_canvas.create_image(int(root.screen_width * 0.475), int(root.screen_height / 5), anchor=tk.NW, image=root.name_input_photo)
        root.background_canvas.create_image(int(root.screen_width * 0.475), int(root.screen_height / 3), anchor=tk.NW, image=root.room_code_photo)

        
       # Create input field
        root.name_entry = ttk.Entry(root.background_canvas)
        root.name_entry.place(x=int(root.screen_width * 0.46), y=int(root.screen_height / 4))

        create_button = ttk.Button(
        root.background_canvas, image=root.join_room_btn_photo, command=root.join_room)
        create_button.place(x=int(root.screen_width * 0.45), y=int(root.screen_height * 0.6))

        root.code_entry = ttk.Entry(root.background_canvas)
        root.code_entry.place(x=int(root.screen_width * 0.46), y=int(root.screen_height * 0.4))

        create_button = ttk.Button(
        root.background_canvas, image=root.back_btn_photo, command=root.menu_manager.show_main_menu)
        create_button.place(x=int(root.screen_width * 0.45), y=int(root.screen_height * 0.7))

    def create_widgets(root):
        name_label = ttk.Label(root, text="Name:")
        name_label.pack()
        root.name_entry = ttk.Entry(root)
        root.name_entry.pack()

        code_label = ttk.Label(root, text="Room Code:")
        code_label.pack()
        root.code_entry = ttk.Entry(root)
        root.code_entry.pack()

        join_button = ttk.Button(
            root, text="Join Room", command=root.join_room)
        join_button.pack()

        back_button = ttk.Button(
            root, text="Back to Menu", command=root.menu_manager.show_main_menu)
        back_button.pack()

    def join_room(root):
        name = root.name_entry.get()
        room_code = root.code_entry.get()
        # Code for joining a room goes here
        # You can update the window or perform any other actions
        root.menu_manager.name = name
        print(f'Set player name to: {root.menu_manager.name}')

        root.menu_manager.room_id = room_code
        print(f'Set room id to: {root.menu_manager.room_id}')

        send_data = {
            'command': "CHECK ROOM",
            'room_id': room_code,
            'name': name,
        }

        root.menu_manager.socket.send(pickle.dumps(send_data))
        print(f'Send data to server: {send_data}')

        data = root.menu_manager.socket.recv(2048)
        data = pickle.loads(data)

        if data['status'] == 'DOES NOT EXIST':
            messagebox.showerror("Error", "Room does not exist.")
        else:
            send_data = {
                'command': "JOIN ROOM",
                'room_id': room_code,
                'name': name,
            }

            root.menu_manager.socket.send(pickle.dumps(send_data))
            print(f'Send data to server: {send_data}')

            root.menu_manager.menus["waiting_room"] = waiting(
                root.menu_manager, root.menu_manager)
            root.menu_manager.show_menu("waiting_room")
