import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())

    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0")
        return

    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    result_var.set(password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and pack widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=50)

length_entry = tk.Entry(root)
length_entry.pack(pady=50)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=100)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Courier", 12))
result_label.pack()

# Start the GUI main loop
root.mainloop()
