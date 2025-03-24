import os
import time
from tkinter import messagebox

def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operation = operation_var.get()
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Divison by zero is not allowed.")
        else:
            messagebox.showwarning("Warning", "Invalid operation selected.")
        
        answer_label.config(text=f"Answer: {result:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tkinter.Tk()
root.title("Math Calculator")
root.geometry("300x150")

tkinter.Label(root, text="Enter first number:").pack(side='left')
num1_entry = tkinter.Entry(root)
num1_entry.pack(side='right')

tkinter.Label(root, text="Enter second number:").pack(side='left')
num2_entry = tkinter.Entry(root)
num2_entry.pack(side='right')

operation_var = tkinter.StringVar()
operation_menu = tkinter.OptionMenu(root, operation_var, 'add', 'subtract', 'multiply', 'divide', '/').pack()

answer_label = tkinter.Label(root, text="")
answer_label.pack()

calculate_button = tkinter.Button(root, text="Calculate", command=calculate).pack(side='left')

tkinter.mainloop()
