from tkinter import *
from PIL import Image, ImageTk
import random


def update_countdown(count):
    countdown.config(text=str(count)) 
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    if count > 0:
        root.after(1000, update_countdown, count - 1)
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        user1.config(image = image1[x])
        tulisan1.config(text = tulisan[x])
        


    else :
        countdown.config(text="Time's Up!") 
        Semut_button.config(state="disabled")
        Orang_button.config(state="disabled")
        Gajah_button.config(state="disabled")
        if(tulisan1.cget("text") == "Semut"):
            if(tulisan2.cget("text") == "Orang"):
                result.config(text="Player 1 Menang!")
            elif(tulisan2.cget("text") == "Gajah"):
                result.config(text="Player 2 Menang!")
            else:
                result.config(text="Seri!")

        elif(tulisan1.cget("text") == "Orang"):
            if(tulisan2.cget("text") == "Gajah"):
                result.config(text="Player 1 Menang!")
            elif(tulisan2.cget("text") == "Semut"):
                result.config(text="Player 2 Menang!")
            else:
                result.config(text="Seri!")

        elif(tulisan1.cget("text") == "Gajah"):
            if(tulisan2.cget("text") == "Semut"):
                result.config(text="Player 1 Menang!")
            elif(tulisan2.cget("text") == "Orang"):
                result.config(text="Player 2 Menang!")
            else:
                result.config(text="Seri!")


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
SOG1 = ImageTk.PhotoImage(Image.open("aset/Jari lengkap.png").resize((300, 300)).rotate(180))
SOG2 = ImageTk.PhotoImage(Image.open("aset/Jari lengkap.png").resize((300, 300)))
image1 = [Gajah1, Orang1, Semut1]
image2 = [Gajah2, Orang2, Semut2]
tulisan = ["Gajah", "Orang", "Semut"]


user1 = Label(root, image=SOG1, background="#9b59b6")
user2 = Label(root, image=SOG2, background="#9b59b6")

tulisan1 = Label(root, text="Semut", font=100, bg="#9b59b6", fg="white" )
tulisan2 = Label(root, text="Orang", font=100, bg="#9b59b6", fg="white" )
tulisan3 = Label(root, text="Gajah", font=100, bg="#9b59b6", fg="white" )
opponent = Label(root, text="OPPONENT", font=100, bg="#9b59b6", fg="white" )

result = Label(root, text="", font=100, bg="#9b59b6", fg="white" )

countdown = Label(root, text="", font= 500, bg="#9b59b6", fg="black")

Semut_button = Button(root, text="Semut", font=100, bg="#9b59b6", fg="white", command=switch_to_Semut2)
Orang_button = Button(root, text="Orang", font=100, bg="#9b59b6", fg="white", command=switch_to_Orang2)
Gajah_button = Button(root, text="Gajah", font=100, bg="#9b59b6", fg="white", command=switch_to_Gajah2)

opponent.grid(row=1, column = 5)
user1.grid(row=2, column=5)
tulisan1.grid(row=3, column=5)
countdown.grid(row = 4, column=5)
tulisan2.grid(row=9, column=5)
user2.grid(row=10, column=5)
result.grid(row=12, column=5)
Semut_button.grid(row=11, column=4)
Orang_button.grid(row=11, column=5)
Gajah_button.grid(row=11, column=6)

update_countdown(10)
root.mainloop()