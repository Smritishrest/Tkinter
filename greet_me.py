import tkinter as tk
def on_button():
    label.config(text = "Hello," + entry.get() + "  How are you")
    
#create a window
window = tk.Tk()
#create a label
label = tk.Label(window, text = "Enter your name ")
label.pack(pady =20)
#create entry widget
entry = tk.Entry(window)
entry.pack(pady =10)

#create command when called 
button =tk.Button(window, text ="Greet me ", command = on_button)
button.pack(pady =10)


window.mainloop()