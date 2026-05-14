import pandas as pd
import tkinter as tk
from tkinter import ttk

# ---------------------------------------------------------
# 1. PRINT FULL ASCII TABLE (0–255)
# ---------------------------------------------------------
def print_full_ascii():
    print(f"{'Char':<6} {'Dec':<6} {'Hex':<6}")
    print("-" * 22)

    for code in range(256):
        char = chr(code) if 32 <= code <= 126 else "."
        print(f"{char:<6} {code:<6} {hex(code):<6}")


# ---------------------------------------------------------
# 2. CREATE ASCII TABLE AS A PANDAS DATAFRAME
# ---------------------------------------------------------
def create_ascii_dataframe():
    data = {
        "Char": [],
        "Decimal": [],
        "Hex": []
    }

    for code in range(256):
        char = chr(code) if 32 <= code <= 126 else "."
        data["Char"].append(char)
        data["Decimal"].append(code)
        data["Hex"].append(hex(code))

    df = pd.DataFrame(data)
    print("\nPandas DataFrame created successfully.")
    print(df.head(10))  # preview
    return df


# ---------------------------------------------------------
# 3. TKINTER GUI VERSION (scrollable table)
# ---------------------------------------------------------
def create_ascii_gui():
    root = tk.Tk()
    root.title("ASCII Table Viewer")
    root.geometry("400x500")

    columns = ("Char", "Dec", "Hex")
    tree = ttk.Treeview(root, columns=columns, show="headings", height=25)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")

    # Insert ASCII rows
    for code in range(256):
        char = chr(code) if 32 <= code <= 126 else "."
        tree.insert("", "end", values=(char, code, hex(code)))

    # Scrollbar
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)

    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()


# ---------------------------------------------------------
# 4. SIMPLE TEXT MENU TO CHOOSE WHAT TO RUN
# ---------------------------------------------------------
def main_menu():
    df = None  # store DataFrame if created

    while True:
        print("\n=== ASCII TOOL MENU ===")
        print("1. Print full ASCII table")
        print("2. Create ASCII DataFrame")
        print("3. Open Tkinter ASCII GUI")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print_full_ascii()

        elif choice == "2":
            df = create_ascii_dataframe()

        elif choice == "3":
            create_ascii_gui()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


# ---------------------------------------------------------
# RUN PROGRAM
# ---------------------------------------------------------
if __name__ == "__main__":
    main_menu()
