import tkinter as tk
from tkinter import ttk
import os

# Create main application window
window = tk.Tk()
window.title("File Crawler App")
window.geometry("800x700")
window.resizable(False, False)

# Label for path input
path_label = ttk.Label(window, text="Enter folder path to search:")
path_label.pack(pady=10)

# Entry field for path
path_entry = ttk.Entry(window, width=80)
path_entry.pack(pady=5)

# Text box to display results
output_box = tk.Text(window, height=20, width=150)
output_box.pack(pady=10)

def crawl_files():
    """
    Crawls the directory entered by the user
    and displays all files found.
    """
    # Clear previous results
    output_box.delete("1.0", tk.END)

    # Get path from input field
    path = path_entry.get()

    # Validate path
    if not os.path.isdir(path):
        output_box.insert(tk.END, "❌ Invalid directory path.\n")
        return

    # Walk through directory
    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            output_box.insert(tk.END, full_path + "\n")

# Search button
search_button = ttk.Button(window, text="Search Files", command=crawl_files)
search_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()
