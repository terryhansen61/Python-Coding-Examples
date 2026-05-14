import tkinter as tk
from tkinter import ttk
import subprocess
import platform
import threading
import socket

def is_ip_address(value):
    try:
        socket.inet_aton(value)
        return True
    except socket.error:
        return False


def resolve_host(host):
    """
    Resolves a hostname to an IP address.
    Returns IP address as string, or None if resolution fails.
    """
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        return None


def ping_host(host):
    """Ping a host and return True if reachable."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.returncode == 0
    except Exception:
        return False


def display_result(message):
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, message)
    output_text.config(state="disabled")


def run_ping(host):
    if is_ip_address(host):
        ip_address = host
    else:
        ip_address = resolve_host(host)

    if not ip_address:
        display_result(f"ERROR: Unable to resolve host '{host}'")
        return

    success = ping_host(host)

    status = "SUCCESS" if success else "FAILED"

    display_result(
        f"Host Name: {host}\n"
        f"IP Address: {ip_address}\n"
        f"Ping Status: {status}"
    )


def start_ping():
    host = host_entry.get().strip()
    if not host:
        display_result("Please enter a valid host or IP address.")
        return

    display_result(f"Pinging {host}...\n")
    threading.Thread(target=run_ping, args=(host,), daemon=True).start()


# ---------------- GUI SETUP ---------------- #

window = tk.Tk()
window.title("Ping Host Tool")
window.geometry("500x300")
window.resizable(False, False)

host_label = ttk.Label(window, text="Enter Host or IP Address:")
host_label.pack(pady=10)

host_entry = ttk.Entry(window, width=40)
host_entry.pack()

ping_button = ttk.Button(window, text="Ping Host", command=start_ping)
ping_button.pack(pady=10)

output_text = tk.Text(window, height=8, width=58, state="disabled")
output_text.pack(pady=10)

window.mainloop()
