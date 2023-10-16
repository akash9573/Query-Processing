import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
# Define the ticker symbol for Alphabet Inc. (GOOGL)
ticker = 'GOOGL'
# Define the start and end dates
start_date = '2023-01-01'
end_date = '2023-10-01'
# Fetch historical data from Yahoo Finance
data = yf.download(ticker, start=start_date, end=end_date)
# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Close Price')
plt.title(f'Historical Stock Prices of {ticker} between {start_date} and {end_date}')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
