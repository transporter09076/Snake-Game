import sqlite3
from tkinter import*
import saaaaaap

root = Tk()
root.title("Snake game")

data = sqlite3.connect("snake.db")
crsr = data.cursor()

crsr.execute("CREATE TABLE IF NOT EXISTS Leaderboard(name VARCHAR(50),\
score INT(3))")

def add_player():
    data = sqlite3.connect("snake.db")
    crsr = data.cursor()
    score = saaaaaap()
    # crsr.execute("INSERT INTO Leaderboard")

root.geometry("600x200")

Label(root,text = "Enter your name", font=("Candara", 16, "normal")).pack(pady=10)
n = Entry(root, font=("Candara", 16, "normal"))
n.pack(pady=10)
btn = Button(root,text = "Confirm",bg = "Blue",fg = "White", font=("Candara", 12, "normal"),command=add_player)
btn.pack(pady=10)


root.mainloop()


