import tkinter as tk
import time

window = tk.Tk()
window.title("Stopwatch")
window.geometry("300x200")
window.resizable(False, False)

start_time = 0
elapsed_time = 0
running = False

time_label = tk.Label(window, text="00:00:00", font=("Arial", 30))
time_label.pack(pady=20)

def format_time(seconds):
    minutes = int(seconds // 60)
    seconds = seconds % 60
    milliseconds = int((seconds - int(seconds)) * 100)
    return f"{minutes:02}:{int(seconds):02}:{milliseconds:02}"

def update_time():
    global elapsed_time
    if running:
        elapsed_time = time.time() - start_time
        time_label.config(text=format_time(elapsed_time))
        window.after(10, update_time)

def start():
    global start_time, running
    if not running:
        start_time = time.time() - elapsed_time
        running = True
        update_time()

def stop():
    global running
    running = False

def reset():
    global elapsed_time, running
    running = False
    elapsed_time = 0
    time_label.config(text="00:00:00")

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Start", width=8, command=start).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Stop", width=8, command=stop).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Reset", width=8, command=reset).grid(row=0, column=2, padx=5)

window.mainloop()
