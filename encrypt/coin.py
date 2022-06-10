#pip install python-binance

import mplfinance as mpl


import pandas as pd

from binance.client import Client
api_key = "yvBrMmxlBUytm0eB8DV636596V7ytvzzhCCI3wJn0wbLqeB19tsTYKpLJWbMWkC1"
api_secret = "hIduzLUoowVH8LsqU4TA0ccE4uWX9W29KT4phsCeh1aNcXj9aaiT6IKWRoAyy9Kj"
client = Client(api_key, api_secret)

def encrypt(coin):
    #抓你想要看的虛擬幣種
    info = client.get_all_tickers()
    df = pd.DataFrame(client.get_all_tickers())
    df = df.set_index("symbol")
    df["price"] = df["price"].astype("float")
    df.index = df.index.astype("string")
    #我想要btc
    print(df.loc[coin])
    print("============================")
    #我想要eth
    print(df.loc[coin])
    print("============================")
    #我想要bnb
    print(df.loc[coin])
    print("============================")

    #btc usdt的幣種圖
    asset = coin
    start = "2021/10/01"
    end = "2022/1/3"
    timeframe = "1d"
    da = pd.DataFrame(client.get_historical_klines(asset, timeframe, start, end))
    da = da.iloc[:, :6]
    da.columns = ["Date", "Open", "High", "Low", "Close", "Volume"]
    da = da.set_index("Date")
    da.index = pd.to_datetime(da.index, unit="ms")
    da = da.astype("float")
    print(da)
    mpl.plot(da, type='candle', volume=True, mav=7)
    return

encrypt("BTCUSDT")
#BTCUSDT 比特幣
#ETHUSDT 以太坊
#BNBUSDT 幣安幣
#DOTUSDT
#DOGEUSDT 狗狗幣
#SRMUSDT
#LTCUSDT
#ZILUSDT
