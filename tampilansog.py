from tkinter import *
from PIL import Image, ImageTk
import random
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.connect((host, port))
# Receive a welcome message from the server
msg = s.recv(1024).decode() 
print(msg)

# Receive the prompt to enter a room code or create a new one
msg = s.recv(1024).decode() 
print(msg)



def update_countdown(count):
    countdown.config(text=str(count)) 
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    if count > 0:
        root.after(1000, update_countdown, count - 1)
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        user1.config(image = image0[x])


    else :
        countdown.config(text="Time's Up!") 
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        user1.config(image = image1[x])
        tulisan1.config(text = tulisan[x])
        # random choice if do not choose
        if(tulisan2.cget("text") == "??"): 
            user2.config(image = image2[y])
            tulisan2.config(text = tulisan[y])
        
        elif(tulisan2.cget("text") == "Semut"):
            s.send("Semut".encode())

        elif(tulisan2.cget("text") == "Orang"):
            s.send("Orang".encode())

        elif(tulisan2.cget("text") == "Gajah"):
            s.send("Gajah".encode())
        
        Semut_button.config(state="disabled")
        Orang_button.config(state="disabled")
        Gajah_button.config(state="disabled")

def switch_to_Semut1():
    user1.config(image=Semut1)
    tulisan1.config(text="Semut")

def switch_to_Orang1():
    user1.config(image=Orang1)
    tulisan1.config(text="Orang")

def switch_to_Gajah1():
    user1.config(image=Gajah1)
    tulisan1.config(text="Gajah")

def switch_to_Semut2():
    user2.config(image=Semut2) 
    tulisan2.config(text="Semut")

def switch_to_Orang2():
    user2.config(image=Orang2)
    tulisan2.config(text="Orang")

def switch_to_Gajah2():
    user2.config(image=Gajah2)
    tulisan2.config(text="Gajah")

def create_room():
    s.send("create".encode())
    msg = s.recv(1024).decode() 
    print(msg)
    room_code_label.config(text="Room Code: ")
    room_code_entry.config(text=msg, state="disabled")
    createroom_button.config(state="disabled")
    countdown.config(text="10")
    update_countdown(10)
    Semut_button.config(state="normal")
    Orang_button.config(state="normal")
    Gajah_button.config(state="normal")
    result.config(text="")

def confirm_room():
    s.send("join".encode())
    room_code = room_code_entry.get()
    s.send(room_code.encode())
    msg = s.recv(1024).decode() 
    print(msg)
    if(msg != "Invalid room code. Please try again"):
        room_code_entry.config(state="disabled")
        join_button.config(state="disabled")
        room_code_label.config(text="Room Code: " + room_code)
        countdown.config(text="3")
        update_countdown(2)
        Semut_button.config(state="normal")
        Orang_button.config(state="normal")
        Gajah_button.config(state="normal")
        result.config(text="")


#basenya
root = Tk()
root.title("Semut Orang Gajah")
root.configure(background="#9b59b6")

Gajah1 = ImageTk.PhotoImage(Image.open("aset/Gajah.png").resize((300, 300)).rotate(180))
Gajah2 = ImageTk.PhotoImage(Image.open("aset/Gajah.png").resize((300, 300)))
Orang1 = ImageTk.PhotoImage(Image.open("aset/Orang.png").resize((300, 300)).rotate(180))
Orang2 = ImageTk.PhotoImage(Image.open("aset/Orang.png").resize((300, 300)))
Semut1 = ImageTk.PhotoImage(Image.open("aset/Semut.png").resize((300, 300)).rotate(180))
Semut2 = ImageTk.PhotoImage(Image.open("aset/Semut.png").resize((300, 300)))

GajahHilang = ImageTk.PhotoImage(Image.open("aset/Gajah hilang.png").resize((300, 300)).rotate(180))
OrangHilang = ImageTk.PhotoImage(Image.open("aset/Orang hilang.png").resize((300, 300)).rotate(180))
SemutHilang = ImageTk.PhotoImage(Image.open("aset/Semut hilang.png").resize((300, 300)).rotate(180))

SOG1 = ImageTk.PhotoImage(Image.open("aset/Jari lengkap.png").resize((300, 300)).rotate(180))
SOG2 = ImageTk.PhotoImage(Image.open("aset/Jari lengkap.png").resize((300, 300)))
image0 = [GajahHilang, OrangHilang, SemutHilang]
image1 = [Gajah1, Orang1, Semut1]
image2 = [Gajah2, Orang2, Semut2]
tulisan = ["Gajah", "Orang", "Semut"]

room_code_entry = Entry(root, width=10, font=100)

user1 = Label(root, image=SOG1, background="#9b59b6")
user2 = Label(root, image=SOG2, background="#9b59b6")

tulisan1 = Label(root, text="??", font=100, bg="#9b59b6", fg="white" )
tulisan2 = Label(root, text="??", font=100, bg="#9b59b6", fg="white" )
opponent = Label(root, text="OPPONENT", font=100, bg="#9b59b6", fg="white" )
room_code_label = Label(root, text="Room Code: ", font=100, bg="#9b59b6", fg="white" )

result = Label(root, text="", font=100, bg="#9b59b6", fg="white" )

countdown = Label(root, text="", font= 500, bg="#9b59b6", fg="black")

Semut_button = Button(root, text="Semut", font=100, bg="#9b59b6", fg="white", command=switch_to_Semut2)
Orang_button = Button(root, text="Orang", font=100, bg="#9b59b6", fg="white", command=switch_to_Orang2)
Gajah_button = Button(root, text="Gajah", font=100, bg="#9b59b6", fg="white", command=switch_to_Gajah2)
createroom_button = Button(root, text="Create", font=100, bg="#9b59b6", fg="white", command=create_room)
join_button = Button(root, text="Join", font=100, bg="#9b59b6", fg="white", command=confirm_room) 

opponent.grid(row=1, column = 5)
createroom_button.grid(row=0, column=5)
room_code_entry.grid(row=0, column=8)
room_code_label.grid(row=0, column=7)
join_button.grid(row=0, column=8)
user1.grid(row=2, column=5)
tulisan1.grid(row=3, column=5)
countdown.grid(row = 4, column=5)
tulisan2.grid(row=9, column=5)
user2.grid(row=10, column=5)
result.grid(row=12, column=5)
Semut_button.grid(row=11, column=4)
Orang_button.grid(row=11, column=5)
Gajah_button.grid(row=11, column=6)

root.mainloop()