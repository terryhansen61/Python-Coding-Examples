import subprocess
import re
import random
import tkinter as tk
import math
import threading
import time

# ---------------------------------------------------------
# WiFi Scanner (Windows netsh)
# ---------------------------------------------------------
def scan_wifi():
    try:
        output = subprocess.check_output(
            ["netsh", "wlan", "show", "networks", "mode=bssid"],
            shell=True, text=True, encoding="utf-8"
        )
    except Exception as e:
        print("Error scanning WiFi:", e)
        return []

    networks = []
    ssid = None

    for line in output.splitlines():
        ssid_match = re.search(r"SSID \d+ : (.*)", line)
        if ssid_match:
            ssid = ssid_match.group(1).strip()

        signal_match = re.search(r"Signal\s*:\s*(\d+)%", line)
        if signal_match and ssid:
            signal = int(signal_match.group(1))
            networks.append((ssid, signal))

    return networks


# ---------------------------------------------------------
# Radar Display
# ---------------------------------------------------------
class RadarScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("WiFi Radar Scanner")

        self.canvas = tk.Canvas(root, width=600, height=600, bg="black")
        self.canvas.pack()

        self.center = (300, 300)
        self.radius = 250

        self.draw_radar_grid()
        self.update_radar()

    def draw_radar_grid(self):
        cx, cy = self.center

        # Circles
        for r in range(50, 301, 50):
            self.canvas.create_oval(cx - r, cy - r, cx + r, cy + r,
                                    outline="green", width=1)

        # Cross lines
        self.canvas.create_line(cx, cy - self.radius, cx, cy + self.radius, fill="green")
        self.canvas.create_line(cx - self.radius, cy, cx + self.radius, cy, fill="green")

    def update_radar(self):
        self.canvas.delete("wifi")

        networks = scan_wifi()

        for ssid, signal in networks:
            angle = random.uniform(0, 2 * math.pi)
            distance = (100 - signal) * 2.5  # weaker signal = farther away

            x = self.center[0] + distance * math.cos(angle)
            y = self.center[1] + distance * math.sin(angle)

            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5,
                                    fill="cyan", outline="", tags="wifi")
            self.canvas.create_text(x + 10, y, text=f"{ssid} ({signal}%)",
                                    fill="white", anchor="w", tags="wifi")

        self.root.after(3000, self.update_radar)  # refresh every 3 seconds


# ---------------------------------------------------------
# Run App
# ---------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    RadarScreen(root)
    root.mainloop()
