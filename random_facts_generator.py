import randfacts as rf
import tkinter as tk
from tkinter import ttk as ttk


window = tk.Tk()
window.title("Random Facts")
window.geometry("600x600")
window.resizable(False, False)

title_label = tk.Label(window, text="Random Facts")
title_label.pack()

# Text box to display results
output_box = tk.Text(window, height=20, width=150)
output_box.pack(pady=10)

def get_random_fact():
    # Clear previous results
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, rf.get_fact())

# Search button
search_button = ttk.Button(window, text="Get Random Fact", command=get_random_fact)
search_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()
