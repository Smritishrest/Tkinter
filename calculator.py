from tkinter import *
import tkinter as tk
def button(num):
   global equation_text
   equation_text = equation_text +  str(num)
   equation_label.set(equation_text)
   pass
def equals():
    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""

    
    pass

def clear():
    
    global equation_text

    equation_label.set("")

    equation_text = ""
    pass

window = tk.Tk()
window.title("Calculator program")
window.geometry("500x500")

equation_text = ""
equation_label= StringVar()

label = tk.Label(window, textvariable=equation_label ,height=2, width = 20, font= "Arial", bg = "white")
label.pack(pady = 10) 

frame = tk.Frame(window)
frame.pack()

button1 = tk.Button(frame, text = 1, height = 3, width = 5, font=35 ,command =lambda: button(1))
button1.grid(row =0, column=0)

button2 = tk.Button(frame, text = 2, height = 3, width = 5, font=35 ,command =lambda: button(2))
button2.grid(row =0, column=1)

button3 = tk.Button(frame, text = 3, height = 3, width = 5, font=35 ,command =lambda: button(3))
button3.grid(row =0, column=2)

button4 = tk.Button(frame, text = 4, height = 3, width = 5, font=35 ,command =lambda: button(4))
button4.grid(row =1, column=0)

button5 = tk.Button(frame, text = 5, height = 3, width = 5, font=35 ,command =lambda: button(5))
button5.grid(row =1, column=1)

button6 = tk.Button(frame, text = 6, height = 3, width = 5, font=35 ,command =lambda: button(6))
button6.grid(row =1, column=2)

button7 = tk.Button(frame, text = 7, height = 3, width = 5, font=35 ,command =lambda: button(7))
button7.grid(row =2, column=0)

button8 = tk.Button(frame, text = 8, height = 3, width = 5, font=35 ,command =lambda: button(8))
button8.grid(row =2, column=1)

button9 = tk.Button(frame, text = 9, height = 3, width = 5, font=35 ,command =lambda: button(9))
button9.grid(row =2, column=2)

plus = tk.Button(frame, text = '+', height = 3, width = 5, font=35 ,command =lambda: button('+'))
plus.grid(row =3, column=0)

minus= tk.Button(frame, text = '-', height = 3, width = 5, font=35 ,command =lambda: button('-'))
minus.grid(row =3, column=1)

multiply = tk.Button(frame, text = '*', height = 3, width = 5, font=40 ,command =lambda: button('*'))
multiply.grid(row =3, column=2)

divide = tk.Button(frame, text = "/", height = 3, width = 5, font=40 ,command =lambda: button("/"))
divide.grid(row =4, column=0)

clear = tk.Button(frame, text = 'CLR', height = 3, width = 5, font=40 ,command =clear)
clear.grid(row =4, column=1)

equals = tk.Button(frame, text = "=", height = 3, width = 5, font=40 ,command = equals)
equals.grid(row =4, column=2)
window.mainloop()
