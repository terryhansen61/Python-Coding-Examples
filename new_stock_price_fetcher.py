import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime


def plot_stocks():
    symbols = ticker_entry.get().upper().replace(" ", "").split(",")
    symbols = [s for s in symbols if s]

    start = start_entry.get()
    end = end_entry.get()

    # Validate dates
    try:
        datetime.strptime(start, "%Y-%m-%d")
        datetime.strptime(end, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Invalid Date", "Dates must be in YYYY-MM-DD format.")
        return

    if not symbols:
        messagebox.showerror("No Symbols", "Please enter at least one stock symbol.")
        return

    plt.figure(figsize=(10, 6))

    for symbol in symbols:
        try:
            data = yf.download(symbol, start=start, end=end)
            if data.empty:
                messagebox.showwarning("No Data", f"No data found for {symbol}.")
                continue

            plt.plot(data.index, data["Close"], label=symbol)

        except Exception as e:
            messagebox.showerror("Error", f"Could not retrieve data for {symbol}.\n{e}")

    plt.title("Stock Closing Prices")
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# -----------------------------
# Tkinter UI
# -----------------------------
root = tk.Tk()
root.title("Stock Plotter")
root.geometry("400x250")

frame = ttk.Frame(root, padding=15)
frame.pack(fill="both", expand=True)

# Stock symbol input
ttk.Label(frame, text="Stock Symbols (comma-separated):").pack(anchor="w")
ticker_entry = ttk.Entry(frame)
ticker_entry.pack(fill="x")

# Start date
ttk.Label(frame, text="Start Date (YYYY-MM-DD):").pack(anchor="w")
start_entry = ttk.Entry(frame)
start_entry.pack(fill="x")

# End date
ttk.Label(frame, text="End Date (YYYY-MM-DD):").pack(anchor="w")
end_entry = ttk.Entry(frame)
end_entry.pack(fill="x")

# Plot button
plot_button = ttk.Button(frame, text="Plot Stocks", command=plot_stocks)
plot_button.pack(pady=10)

root.mainloop()
