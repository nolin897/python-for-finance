import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

yf.pdr_override()

stock=input("Enter a stock ticker symbol: ")
print(stock)

startyear=2019
startmonth=1
startday=1

start=dt.datetime(startyear,startmonth,startday)

now=dt.datetime.now()

df=pdr.get_data_yahoo(stock,start,now)

ma=50

smaString="Sma_"+str(ma)

df[smaString]=df.iloc[:,4].rolling(window=ma).mean()
#creates new column with the name smaString, and that column is the rolling moving average
#...with a window size of our moving average which is 50 days and that is made from the fourth
#...column in DF currently which is the adjusted close
#...this is how you create a simple moving average in python using pandas

df=df.iloc[ma:]

numH=0
numC=0

for i in df.index:
    if(df["Adj Close"][i]>df[smaString][i]):
        print("The Close is higher")
        numH+=1
    else:
        print("The Close is lower")
        numC+=1

print(str(numH))
print(str(numC))

    #DATES are the index column of the dataframe
    #we want to access the ith value of the moving average and also the adjusted close
    #so we can compare the two so there are a couple ways we can access these values
    #first is with iloc
    #WE COMPARED THE CLOSE AND THE SIMPLE MOVING AVG