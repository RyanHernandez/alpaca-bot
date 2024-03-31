import csv
from datetime import datetime, timedelta
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data import TimeFrame 
import matplotlib.pyplot as plt

api_key = 'PKQCPX33TGNDVKORODIS'
api_secret = 'RHISFz5oidO3ZxB1meme6LDnxJAzdHhgv8jIhJ9O'
market_client = StockHistoricalDataClient(api_key, api_secret)

with open('symbols.csv') as symbols: 
    reader = csv.reader(symbols)
    reader.__next__()
    
    a = []
    for symbol in reader:
        a.append(symbol[0])
        
    hist_days = 1
    today = datetime.now()
    n_days_ago = today - timedelta(days=hist_days)
    
    market_request = StockBarsRequest(symbol_or_symbols=a,
                        start=n_days_ago,
                        end=today,
                        adjustment='raw',
                        feed='sip',
                        timeframe=TimeFrame.Day)
    
    market_data_df = market_client.get_stock_bars(market_request).df
    market_data_df.columns = market_data_df.columns.to_flat_index()
    market_data_df.reset_index(inplace=True)
    
    cols = ["symbol", "timestamp", "open", "high", "low", "close", "volume", "trade_count", "vwap"]
    
    with open('data.csv', 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(cols)
        for value in market_data_df.values:
            writer.writerow(value)