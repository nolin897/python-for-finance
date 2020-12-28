
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
from pandas import ExcelWriter

yf.pdr_override()
start=dt.datetime(2017,12,1)
now=dt.datetime.now()

print(os.getcwd())

filePath=r"/Users/nicholasolin/Documents/GitHub/python-for-finance/RichardStocks.xlsx"

stocklist=pd.read_excel(filePath) #converting the Excel data into a pandas dataframe
stocklist=stocklist.head() #using the first 5 stocks out of the pandas dataframe 

exportList=pd.DataFrame(columns=['Stock', "RS_Rating", "50 Day MA", "150 Day MA", "200 Day MA", "52 Week Low", "52 Week High"])
#saving all the stocks that meet the criteria to list exportList as a pandas dataframe

for i in stocklist.index: #accessing all the different stocks in the index
    stock=str(stocklist["Symbol"][i]) #saving the symbol as the variable stock
    RS_Rating=stocklist["RS Rating"][i] #saving the RS rating in the column for that stock

    try:
        df=pdr.get_data_yahoo(stock,start,now) #creating a dataframe with the open, high, low, adj close for that stock

        smaUsed=[50,150,200] #in this list is the 50, 150, and 200 day moving averages
        for x in smaUsed: #for loop creates moving averages for each of these values
            sma=x
            df["SMA_"+str(sma)]=round(df.iloc[:4].rolling(window=sma).mean(),2) #calculating all three of these simple moving averages very quickly

        currentClose=df["Adj Close"][-1] #getting the last adjusted close, accessing the most recent adj close in the yahoo finance database
        moving_average_50=df["SMA_50"][-1]
        moving_average_150=df["SMA_150"][-1]
        moving_average_200=df["SMA_200"][-1]
        low_of_52week=min(df["Adj Close"][-260:]) #finding the minimum of the last 260 adj closes
        high_of_52week=max(df["Adj Close"][-260:]) #finding the maximum of the last 260 adj closes

        try: #tells python to try to find the 200 day moving average as of 20 days ago
            moving_average_200_20past=df["SMA_200"][-20]
        except Exception: #and setting it equal to zero if it can't find this value 
            moving_average_200_20past=0

        print("Checking "+stock+"...")
    
    except Exception:
        print("No data on "+stock)