import tkinter as tk
from tkinter import ttk
import socket

# Import Class
from menu import menu
from maininit import maininit
from createroom import createroom
from join import join
from room import room
# from sog import sog
# from tampilan import tampilan


class Main(tk.Tk):
    def __init__(root):
        super().__init__()
        root.menus = {}
        root.socket = None
        root.name = None
        root.room_id = None
        root.connect_to_server()
        root.create_menu_instances()
        root.current_menu = None
        root.show_main_menu()
        root.configure_style()

    def connect_to_server(root):
        try:
            # Update with the server address and port
            server_address = ('localhost', 5000)
            root.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            root.socket.connect(server_address)
            # Perform any other actions with the connected socket if needed
            print("Connect to server")
        except ConnectionError:
            # Handle connection error
            pass

    def create_menu_instances(root):
        root.menus["main"] = maininit(root, root)
        root.menus["play"] = menu(root, root)
        root.menus["create"] = createroom(root, root)
        root.menus["join"] = join(root, root)
        # root.menus["sog"] = sog(root, root)

    def configure_style(root):
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12))
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))

    def show_main_menu(root):
        root.show_menu("main")

    def show_menu(root, menu_name):
        if root.current_menu:
            root.current_menu.pack_forget()
        root.current_menu = root.menus[menu_name]
        root.current_menu.pack(expand=True)


if __name__ == "__main__":
    menu_manager = Main()
    menu_manager.mainloop()
