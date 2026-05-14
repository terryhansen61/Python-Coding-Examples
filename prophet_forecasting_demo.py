from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "ds":pd.date_range(start='2023-01-01',periods=30),
    "y":[20,21,19,22,24,23,25,26,27,29,
        28,30,31,33,32,34,35,26,38,37,
        39,40,41,41,43,45,44,46,47,48]})

model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=10)
forecast = model.predict(future)
model.plot(forecast)
plt.show()
