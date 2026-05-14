import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")
window.resizable(False, False)


def button_click(value):
    """
    Adds the pressed button's value to the display
    """
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + str(value))

def clear_display():
    """
    Clears the calculator display
    """
    display.delete(0, tk.END)

def calculate():
    """
    Evaluates the expression in the display
    """
    try:
        expression = display.get()
        result = eval(expression)  # Evaluate math expression
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def create_button(text, row, column):
    """
    Creates a calculator button
    """
    return tk.Button(
        window,
        text=text,
        width=5,
        height=2,
        font=("Arial", 14),
        command=lambda: button_click(text)
    ).grid(row=row, column=column, padx=5, pady=5)

def key_press(event):
    """
    Handles keyboard input for the calculator
    """
    key = event.char
    keysym = event.keysym

    # Allow numbers and operators
    if key in "0123456789+-*/.":
        button_click(key)

    # Enter key calculates result
    elif keysym == "Return":
        calculate()

    # Backspace deletes last character
    elif keysym == "BackSpace":
        current = display.get()
        display.delete(0, tk.END)
        display.insert(0, current[:-1])

    # Escape clears the screen
    elif keysym == "Escape":
        clear_display()


# Entry widget for displaying numbers and results
display = tk.Entry(
    window,
    width=16,
    font=("Arial", 24),
    borderwidth=5,
    relief="ridge",
    justify="right"
)

# Place the display at the top
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Give focus to the display so it receives keyboard input
display.focus_set()

# Number buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1)
]

for (text, row, col) in buttons:
    create_button(text, row, col)

# Operator buttons
create_button('+', 1, 3)
create_button('-', 2, 3)
create_button('*', 3, 3)
create_button('/', 4, 3)

# Clear button
tk.Button(
    window,
    text="C",
    width=5,
    height=2,
    font=("Arial", 14),
    command=clear_display
).grid(row=4, column=0, padx=5, pady=5)

# Equals button
tk.Button(
    window,
    text="=",
    width=5,
    height=2,
    font=("Arial", 14),
    command=calculate
).grid(row=4, column=2, padx=5, pady=5)

# Bind keyboard events to the window
window.bind("<Key>", key_press)

window.mainloop()
