import yfinance as yf
import matplotlib.pyplot as plt

# Input two stock symbols
symbol1 = input("Enter the first stock symbol: ")
symbol2 = input("Enter the second stock symbol: ")

# Define the time period
start_date = '2012-01-01'
end_date = '2022-12-31'

# Fetch daily and weekly historical data for the first stock
daily_data1 = yf.download(symbol1, start=start_date, end=end_date, interval='1d')
weekly_data1 = yf.download(symbol1, start=start_date, end=end_date, interval='1wk')

# Fetch daily and weekly historical data for the second stock
daily_data2 = yf.download(symbol2, start=start_date, end=end_date, interval='1d')
weekly_data2 = yf.download(symbol2, start=start_date, end=end_date, interval='1wk')

# Create daily line chart for the first stock
plt.figure(figsize=(12, 6))
plt.title(f'{symbol1} Daily Closing Prices')
plt.plot(daily_data1['Close'], label=f'{symbol1} Close Price', marker='o')
plt.plot(daily_data2['Close'], label=f'{symbol2} Close Price', marker='o')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Save the daily line chart as an image
plt.savefig(f'{symbol1}_{symbol2}_daily_prices.png')
plt.show()

# Create weekly line chart for the first stock
plt.figure(figsize=(12, 6))
plt.title(f'{symbol1} Weekly Closing Prices')
plt.plot(weekly_data1['Close'], label=f'{symbol1} Close Price', marker='o')
plt.plot(weekly_data2['Close'], label=f'{symbol2} Close Price', marker='o')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Save the weekly line chart as an image
plt.savefig(f'{symbol1}_{symbol2}_weekly_prices.png')
plt.show()
