import tkinter as tk

# Create the main application window
window = tk.Tk()
window.title("Heartbeat Loading Bar")
window.geometry("400x150")
window.resizable(False, False)

# Canvas for drawing animation
canvas = tk.Canvas(window, width=400, height=150, bg="black")
canvas.pack()

# Initial bar settings
bar_x_start = 50
bar_y_start = 70
bar_height = 20
bar_width = 50

# Draw the heartbeat bar
heartbeat_bar = canvas.create_rectangle(
    bar_x_start,
    bar_y_start,
    bar_x_start + bar_width,
    bar_y_start + bar_height,
    fill="red",
    outline=""
)

# Animation variables
pulse_growing = True
max_width = 300
min_width = 50
pulse_speed = 10

def animate_heartbeat():
    global bar_width, pulse_growing

    if pulse_growing:
        bar_width += pulse_speed
        if bar_width >= max_width:
            pulse_growing = False
    else:
        bar_width -= pulse_speed
        if bar_width <= min_width:
            pulse_growing = True

    canvas.coords(
        heartbeat_bar,
        bar_x_start,
        bar_y_start,
        bar_x_start + bar_width,
        bar_y_start + bar_height
    )

    window.after(50, animate_heartbeat)

# Start animation
animate_heartbeat()

# Run the application
window.mainloop()
