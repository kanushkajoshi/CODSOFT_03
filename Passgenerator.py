import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        password_length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length")
        return
    
    if password_length < 8:
        messagebox.showerror("Error", "Password length must be at least 8")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text=password)

root = tk.Tk()
root.title("Password Generator")

window_width = 500
window_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.config(bg="#f0f0f0")  # Light gray background

# Function to change frame colors
def change_frame_colors(frame, bg_color):
    frame.config(bg=bg_color)
    for child in frame.winfo_children():
        if isinstance(child, tk.Frame):
            change_frame_colors(child, bg_color)
        elif isinstance(child, tk.Label):
            child.config(bg=bg_color)
        elif isinstance(child, tk.Button):
            child.config(bg=bg_color)

# Input Frame
input_frame = tk.Frame(root, bg="#4CAF50", pady=10)
input_frame.pack(pady=20)

length_label = tk.Label(input_frame, text="Enter password length:", font=("Arial", 12), bg="#4CAF50", fg="#FFFFFF")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(input_frame, font=("Arial", 12))
length_entry.grid(row=1, column=0, padx=10, pady=10)  # Placed on the next row

# Output Frame
output_frame = tk.Frame(root, bg="#03A9F4", pady=10)
output_frame.pack(pady=20)

password_label = tk.Label(output_frame, text="", font=("Arial", 16), bg="#03A9F4", fg="#FFFFFF")
password_label.pack(pady=10)

# Generate Password Button
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12), bg="#f44336", fg="#FFFFFF", command=generate_password)
generate_button.pack(pady=10)

# Error message if password length is less than 8
def show_length_error(event):
    try:
        if int(length_entry.get()) < 8:
            length_label.config(text="Enter password length (at least 8):", fg="red")
        else:
            length_label.config(text="Enter password length:", fg="#FFFFFF")
    except ValueError:
        length_label.config(text="Enter password length (at least 8):", fg="red")

length_entry.bind("<KeyRelease>", show_length_error)

root.mainloop()