import alpaca_trade_api as tradeapi
import matplotlib.pyplot as plt
import datetime as dt
import pytz

BASE_URL = "https://paper-api.alpaca.markets"
ALPACA_API_KEY = "PKQCPX33TGNDVKORODIS"
ALPACA_SECRET_KEY = "RHISFz5oidO3ZxB1meme6LDnxJAzdHhgv8jIhJ9O"

# Instantiate REST API Connection
api = tradeapi.REST(key_id=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY, 
                    base_url=BASE_URL, api_version='v2')

# Fetch Account Details
account = api.get_account()
# Print Account Details
print(account.id, account.equity, account.status)

# Fetch Apple data from last n days
n = 100
_bars = api.get_bars('AAPL', 
                     '1D',
                     start=(dt.datetime.now(pytz.timezone('US/Eastern')) - dt.timedelta(days=n)).isoformat(),
                     end=None,
                     limit=n)

# Reformat data (drop multi-index, rename columns, reset index)
data = _bars.df
data.columns = data.columns.to_flat_index()
data.reset_index(inplace=True)
print(data)

# Plot stock price data
plot = data.plot(x="timestamp", y="close", legend=False)
plot.set_xlabel("Date")
plot.set_ylabel("Apple Close Price ($)")
plt.show()