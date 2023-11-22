import tkinter as tk

def button_1():
    task = entry.get()
    if task:
        list.insert(tk.END, task)
        entry.delete(0, tk.END)
    pass

def button_2():
    try:
        selected_task = list.curselection()[0]
        list.delete(selected_task)
    except IndexError:
        

     pass
window = tk.Tk()
label = tk.Label(window, width = 20, bg = 'Gray', fg = "white" ,text ="To Do List")
label.pack()

button_1 = tk.Button(window, text="Add Task",width=10, command = button_1, bg = "black", font = ("Calibri",10),fg = "yellow")
button_1.pack(pady = 5)

button_2 = tk.Button(window, text="Delete task", command = button_2, bg = 'black', font = ("Calibri",10), fg = "yellow")
button_2.pack(pady =5)

entry = tk.Entry(window, width = 20, bg = "white", fg = "violet")
entry.pack(pady = 10)


list = tk.Listbox(window, selectmode = tk.SINGLE, width = 12, height = 5, bg = "white", fg= "violet")
list.pack(pady= 10)

window.title('TO DO LIST')
window.mainloop()