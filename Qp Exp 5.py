import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Step 2: Retrieve historical stock data
ticker = "GOOGL"  # Ticker symbol for Alphabet Inc.
start_date = "2023-01-01"
end_date = "2023-10-01"

# Using yfinance to get the stock data
data = yf.download(ticker, start=start_date, end=end_date)

# Step 3: Filter the data for the desired date range
# Since we're interested in trading volume, we only need that column
data = data['Volume']

# Step 4: Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(data.index, data.values, color='blue', alpha=0.7)
plt.title(f'Trading Volume of {ticker} between {start_date} and {end_date}')
plt.xlabel('Date')
plt.ylabel('Trading Volume')
plt.show()
