import yfinance as yf
from matplotlib import pyplot as plt

apple_data = yf.download("AAPL", start="2026-01-01", end="2026-03-12")
google_data = yf.download("GOOG", start="2026-01-01", end="2026-03-12")
microsoft_data = yf.download("MSFT", start="2026-01-01", end="2026-03-12")

"""
# This prints out the first 5 rows of each data set so you can see the data
print(apple_data.head())
print(google_data.head())
"""

plt.figure(figsize = (8, 8))

plt.plot(apple_data.Close, label = "Apple", color = 'blue', marker = 'o')
plt.plot(google_data.Close, label = "Google", color = 'red', marker = 'x')
plt.plot(microsoft_data.Close, label = "Microsoft", color = 'green', marker = 'v')
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title("Stock Closing Price History")

# Add legend
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
