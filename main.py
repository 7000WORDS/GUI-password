from tkinter import *
import tkinter as tk
from tkinter import messagebox
import webbrowser


username = input("set your username: ")
password = input("set a password: ")

def Ok():

    uname = e1.get()
    pword = e2.get()

    if(uname == "" and pword == ""):
            messagebox.showinfo("", "Blank Not allowed")

    elif(uname == username and pword == password):

            messagebox.showinfo("", "Login Success")
            ruut = Tk()
            ruut.title("Understandable")
            root.destroy()

    else:
            messagebox.showinfo("", "Incorrent Username and Password")


def callback(url):
    webbrowser.open_new("https://youtu.be/dQw4w9WgXcQ")

root = Tk()
link1 = Label(root, text="Google Hyperlink", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("https://youtu.be/dQw4w9WgXcQ"))


root = Tk()
root.title("Login")
root.geometry("300x200")
global e1
global e2

Label(root, text="UserName").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")


Button(root, text="Login", command=Ok, height=3, width=13).place(x=10, y=100)

root.mainloop()
