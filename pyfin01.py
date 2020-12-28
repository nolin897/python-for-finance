import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

yf.pdr_override()

stock=input("Enter a stock ticker symbol: ")
# print(stock)

startyear=2019
startmonth=1
startday=1

start=dt.datetime(startyear,startmonth,startday) # dictates time we want to start at

now=dt.datetime.now() #two datetime objects, start and now

df=pdr.get_data_yahoo(stock,start,now) #getting all that data within the range specified

# print(df)

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

# for i in df.index:
#     print(i) 
    
    #the dates row is the index row of this datafram, so this will print dates
    #for each of these rows we can use that i to determine which i we're talking about
    #we want to be able to access the ith value of the sma and adj close to compare the two

    #one way to do this

# for i in df.index:
#     print(df.iloc[:,4][i])

    #this will print the adjusted close for each date

    #another way to do this using the column heading instead of the column index

# for i in df.index:
#     print(df["Adj Close"][i])

    #now incorporate the moving average variable we created

# for i in df.index:
#     print(df[smaString][i])

#now we compare the Adj Close and the smaString
#for each line item the program went through and checked if Adj Close is higher or lower
#than the moving average and printe the appropriate result

# for i in df.index:
#     if(df["Adj Close"][i]>df[smaString][i]):
#         print("The Close is higher")
#     else:
#         print("The Close is lower")

#now let's take this one step further and count the amount of times Adj Close is
# higher or lower than the moving average

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