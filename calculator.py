# create a simple calculator

import tkinter as tk
from tkinter import ttk, messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y

def calculate():
    operation = operation_var.get()
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    
    try:
        if operation == "Addition":
            result = add(num1, num2)
        elif operation == "Subtraction":
            result = subtract(num1, num2)
        elif operation == "Multiplication":
            result = multiply(num1, num2)
        elif operation == "Division":
            result = divide(num1, num2)
        
        result_label.config(text="Result: " + str(result))
        
        try_again = messagebox.askyesno("Try Again?", "Do you want to try again?")
        if try_again:
            operation_var.set("")  # Reset operation dropdown
            num1_entry.delete(0, tk.END)  # Clear num1 entry
            num2_entry.delete(0, tk.END)  # Clear num2 entry
            result_label.config(text="")
        else:
            messagebox.showinfo("Thank You!", "Thank you for using our calculator!\nHave a great day!")
            root.destroy()
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Calculator App")
root.geometry("300x200")
root.configure(bg="#FFB6C1")

mainframe = ttk.Frame(root, padding="20", style='My.TFrame')
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

style = ttk.Style()
style.configure('My.TFrame', background='#FFB6C1')

operation_var = tk.StringVar()
operation_label = ttk.Label(mainframe, text="Choose operation:", style='My.TLabel')
operation_label.grid(column=1, row=1, sticky=tk.W)
operation_combobox = ttk.Combobox(mainframe, textvariable=operation_var, values=["Addition", "Subtraction", "Multiplication", "Division"], style='My.TCombobox')
operation_combobox.grid(column=2, row=1)

num1_label = ttk.Label(mainframe, text="Enter first number:", style='My.TLabel')
num1_label.grid(column=1, row=2, sticky=tk.W)
num1_entry = ttk.Entry(mainframe)
num1_entry.grid(column=2, row=2)

num2_label = ttk.Label(mainframe, text="Enter second number:", style='My.TLabel')
num2_label.grid(column=1, row=3, sticky=tk.W)
num2_entry = ttk.Entry(mainframe)
num2_entry.grid(column=2, row=3)

calculate_button = ttk.Button(mainframe, text="Calculate", command=calculate)
calculate_button.grid(column=2, row=4)

result_label = ttk.Label(mainframe, text="", style='My.TLabel')
result_label.grid(column=2, row=5)

root.mainloop()
