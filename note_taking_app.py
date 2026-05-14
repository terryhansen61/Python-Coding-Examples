import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Untitled - Notes")
        self.root.geometry("700x500")

        self.file_path = None

        # Create text area with scrollbar
        self.text_area = ScrolledText(root, wrap="word", font=("Arial", 12))
        self.text_area.pack(fill="both", expand=True)

        # Create menu bar
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        # File menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

    # -----------------------------
    # File Operations
    # -----------------------------

    def new_file(self):
        self.text_area.delete("1.0", tk.END)
        self.file_path = None
        self.root.title("Untitled - Notes")

    def open_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if path:
            try:
                with open(path, "r", encoding="utf-8") as file:
                    content = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)
                self.file_path = path
                self.root.title(f"{path} - Notes")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file:\n{e}")

    def save_file(self):
        if self.file_path:
            try:
                with open(self.file_path, "w", encoding="utf-8") as file:
                    file.write(self.text_area.get("1.0", tk.END))
                messagebox.showinfo("Saved", "File saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{e}")
        else:
            self.save_as_file()

    def save_as_file(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if path:
            try:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(self.text_area.get("1.0", tk.END))
                self.file_path = path
                self.root.title(f"{path} - Notes")
                messagebox.showinfo("Saved", "File saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{e}")


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
