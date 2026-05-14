import tkinter as tk
from tkinter import messagebox, ttk
import random
import string

# Set the minimum length of the password
pwd_min_length = 8

# Create main window
window = tk.Tk()                                # Generates a window object
window.title("Password Generator")              # Title of the window
window.geometry("400x400")                      # Size of the window upon generation
window.resizable(True, True)        # Is the window resizable or not

# Checks the strength of the password and assigns a numeric value
def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    return score


def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a number.")
        return

    if length < pwd_min_length:
        messagebox.showwarning("Too Short", f"Password should be at least {pwd_min_length} characters.")
        return

    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    # Check strength
    # Takes the input from the score and creates a measure to show and label the password according to strength
    score = check_strength(password)
    strength_bar['value'] = score

    if score <= 2:
        strength_label.config(text="Strength: Weak")
    elif score <= 4:
        strength_label.config(text="Strength: Medium")
    else:
        strength_label.config(text="Strength: Strong")


# UI Elements
title_label = tk.Label(window, text="Password Generator", font=("Arial", 16))
title_label.pack(pady=10)

# These 4 lines create the label, and then create the text box for the length you want the password to be
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack(pady=5)

# These 4 lines create the label, and then create the text box for the output random generated password
password_label = tk.Label(window, text="Generated Password:")
password_label.pack()
password_entry = tk.Entry(window, width=35)
password_entry.pack(pady=5)

# This adds a password strength meter
strength_label = tk.Label(window, text="Strength: ")
strength_label.pack(pady=5)
strength_bar = ttk.Progressbar(
    window,
    length=250,
    maximum=6
)
strength_bar.pack()

generate_button = tk.Button(
    window,
    text="Generate Password",
    command=generate_password
)
generate_button.pack(pady=15)

window.mainloop()
