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

start=dt.datetime(startyear,startmonth,startday) # dictates time we want to start at

now=dt.datetime.now() #two datetime objects, start and now

df=pdr.get_data_yahoo(stock,start,now) #getting all that data within the range specified

print(df)

ma=50

smaString="Sma_"+str(ma)

df[smaString]=df.iloc[:,4].rolling(window=ma).mean()
#creating the column with the name SmaString 
#that column is a rolling moving average with a window size of 50 days
#and that is made form the 4th column in df which is currently is the Adjusted Close
#this is how you create a simple moving average in python using pandas

# print(df)

#the first 50 days don't have values so we cut them out

df=df.iloc[ma:]

# print(df)

#USE for loop 

for i in df.index:
    print(i) 
    
    #the dates row is the index row of this datafram, so this will print dates
    #for each of these rows we can use that i to determine which i we're talking about
    #we want to be able to access the ith value of the sma and adj close to compare the two

    #one way to do this

for i in df.index:
    print[df.iloc[:,4][i]]