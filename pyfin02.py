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

#first we create a lot of exponential moving averages

emasUsed = [3,5,8,10,12,15,30,35,40,45,50,60]

#then we create a for loop that goes through each of these periods and creates a column in our dataframe for each

for x in emasUsed:
    ema=x
    df["Ema_"+str(ema)]=round(df.iloc[:,4].ewm(span=ema, adjust=False).mean(),2)

df=df.iloc[60:]

pos=0 #we will use this variable to help us determine whether or not we're entering a position, entered if =1, not entered if =0
num=0 #help us keep track of the row that we're on
percentchange=[] #an empty list to which we add the results of our trades

for i in df.index:
    cmin=min(
        df["Ema_3"][i],
        df["Ema_5"][i],
        df["Ema_8"][i],
        df["Ema_10"][i],
        df["Ema_12"][i],
        df["Ema_15"][i]
    )
    cmax=max(
        df["Ema_30"][i],
        df["Ema_35"][i],
        df["Ema_40"][i],
        df["Ema_45"][i],
        df["Ema_50"][i],
        df["Ema_60"][i]
    )
    
    close=df["Adj Close"][i]
    
    if(cmin>cmax):
        #if we're in a red-white-blue pattern
        print("Red White Blue")
        if(pos==0): #two equal signs bc we're checking not assigning the value
            bp=close #setting our buy price at the close
            pos=1 #turning on our position in the stock
            print("Buying now at "+str(bp)) #printing out to the user that we are buying now at that price 
    elif(cmin<cmax):
        print("Blue White Red")
        if(pos==1):
            pos=0
            sp=close
            print("Selling now at "+str(sp))
            pc=(sp/bp-1)*100
            percentchange.append(pc) #each time we close a position it will add the pc value to our percentchange list
    if(num==df["Adj Close"].count()-1 and pos==1): #checking whether or not num is equal to the value of the length of our pandas dataframe
        pos=0
        sp=close
        print("Selling now at "+str(sp))
        pc=(sp/bp-1)*100
        percentchange.append(pc)    
    num+=1

print(percentchange)

gains=0
ng=0 #number of gains
losses=0
nl=0 #number of losses
totalR=1 # total returns

for i in percentchange:
    if(i>0): # if it's a winning trade
        gains+=i
        ng+=1
    else:
        losses+=i
        nl+=1
    totalR=totalR*((i/100)+1)

totalR=round((totalR-1)*100,2)
#multiplying all those different percentages together to basically calculate 
# what the total return would be if you were going 100% in and out based 
# on all those different trades, cleaning it up to round to 2 decimal places and 
# output it as a percentage for the user

#Now we calculate avg gain, avg loss, and our win to loss ratio
if(ng>0):
    avgGain=gains/ng
    maxR=str(max(percentchange)) #finding the best trade out of that list and it's saving it as this maxR variable
else:
    avgGain=0
    maxR="undefined"

if(nl>0):
    avgLoss=losses/nl
    maxL=str(min(percentchange)) #finding the wors(?) trade out of that list and it's saving it as this maxL variable
    ratio=str(-avgGain/avgLoss)
else:
    avgLoss=0
    maxL="undefined"
    ratio="inf"

# now calculate our batting average, or the % of the times a trade ended up with a net gain

if(ng>0 or nl>0):
    battingAvg=ng/(ng+nl)
else:
    battingAvg=0

print()
print("Results for "+ stock +" going back to "+str(df.index[0])+", Sample size: "+str(ng+nl)+" trades")
print("EMAs used: "+str(emasUsed))
print("Batting Avg: "+ str(battingAvg))
print("Gain/loss ratio: "+ ratio)
print("Average Gain: "+ str(avgGain))
print("Average Loss: "+ str(avgLoss))
print("Max Return: "+ maxR)
print("Max Loss: "+ maxL)
print("Total return over "+str(ng+nl)+ " trades: "+ str(totalR)+"%" )
#print("Example return Simulating "+str(n)+ " trades: "+ str(nReturn)+"%" )
print()