from tkinter import *
tk = Tk()
tk.title("Test")
tk.mainloop()

username = input("set your username: ")
password = input("set a password: ")

u_name = input("enter your username: ")
while u_name != username:
    print("try again")
    u_name = input()
if u_name == username:
    print("you got it right.")

p_word = input("enter your password: ")
while p_word != password:
    print("try again: ")
    p_word = input()
if p_word == password:
    print("you got it right.")
    