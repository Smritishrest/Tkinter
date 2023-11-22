from tkinter import *
from tkinter import messagebox
def login():
    username = entry1.get()
    password = entry2.get()
    if (username ==" " and password ==" "):
        messagebox.showinfo("blank space not allowed")
    elif(username =="smriti" and password =="shrestha"):
                messagebox.showinfo("login succeded ")
    elif(username =="shrestha" and password =="smriti"):
                messagebox.showinfo("login succeded ")
    else:
                messagebox.showinfo("username or password is incorrect ")

root = Tk()
root.title("Login")
root.geometry('300x200')
global entry1
global entry2

Label(root, text = "Username" ).place(x = 20, y = 20)
Label(root, text = "Password" ).place(x = 20, y = 70)

entry1 = Entry(root, bd = 5)
entry1.place(x = 140, y = 20)


entry2 = Entry(root, bd = 5)
entry2.place(x = 140, y = 70)

Button(root, text = "Login", command = login ,  width = 5, bd = 6).place( x = 100, y = 120)


root.mainloop()