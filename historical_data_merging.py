from AliceBlue_V2 import Alice
import time
import datetime
import pandas as pd
import numpy as np 
import yfinance as yf

# yesterday = datetime.datetime(2023,5,25,10,15)
# today = datetime.datetime(2023,5,30,10,15)
today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=5)


excelFile = pd.read_excel('F:/Ezquant/Historical/Stocks.xlsx')
excelFile.to_csv ("F:/Ezquant/Historical/Stocks.csv", index = None, header=True)
exchange = pd.DataFrame(pd.read_csv("F:/Ezquant/Historical/Stocks.csv"))

print(exchange["Symbol"].values)

trading = exchange["Symbol"].values.tolist()

for symbol in trading:

    data11 = yf.download(f'{symbol}.NS',yesterday,today,interval="1m")
    data11.insert(4, "Symbol", f'{symbol}')

    data11.to_csv(f'F:/Ezquant/Historical/{symbol}-EQ.csv')


 
while(True):
    temp = pd.DataFrame()
    for symbol in trading:
        df2 = pd.read_csv(f'F:/Ezquant/Historical/{symbol}-EQ.csv')
        temp = pd.concat([temp, df2])
        temp.to_csv('F:/Ezquant/Historical/Merged.csv', index=False)
        
    exit(0)



