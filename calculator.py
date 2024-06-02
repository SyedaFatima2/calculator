
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Calculator")
root.config(bg="black") 


display = tk.Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))


def button_clear():
    display.delete(0, tk.END)


def button_equal():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        display.delete(0, tk.END)

def button_backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


 
button_bg = "lightgray"
button_fg = "black"
button_active_bg = "gray"
button_active_fg = "white"


button_1 = tk.Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0))

button_add = tk.Button(root, text="+", padx=20, pady=20, command=lambda: button_click("+"))
button_equal = tk.Button(root, text="=", padx=50, pady=20, command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=10, pady=20, command=button_clear)
button_modulus = tk.Button(root, text="%", padx=18, pady=20, command=lambda: button_click('%'))

button_subtract = tk.Button(root, text="-", padx=21, pady=20, command=lambda: button_click("-"))
button_multiply = tk.Button(root, text="*", padx=21, pady=20, command=lambda: button_click("*"))
button_divide = tk.Button(root, text="/", padx=21, pady=20, command=lambda: button_click("/"))
button_point = tk.Button(root, text=".", padx=21, pady=20, command=lambda: button_click("."))
button_back = tk.Button(root, text="Back", padx=10, pady=20, command=button_backspace)




button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=1)

button_add.grid(row=4, column=3)
button_equal.grid(row=5, column=2, columnspan=2)
button_clear.grid(row=1, column=0)
button_back.grid(row=1, column=1)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)
button_modulus.grid(row=1, column=2)
button_point.grid(row=5, column=0)
root.mainloop()
