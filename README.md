# python-for-finance

Practice and learning based on the youtube tutorials by Richard Moglen: https://www.youtube.com/watch?v=myFD0np9eys&list=PLPfme2mwsQ1FQhH1icKEfiYdLSUHE-Wo5&index=1

Documentation for modules at:

https://numpy.org/

https://pypi.org/project/yfinance/

https://pypi.org/project/pandas-datareader/
https://pandas-datareader.readthedocs.io/en/latest/index.html?highlight=pdr#quick-start

See prof-rossetti github for pandas package resources:
https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/pandas.md

Second Video:
https://www.youtube.com/watch?v=eYK2SNygAog&list=PLPfme2mwsQ1FQhH1icKEfiYdLSUHE-Wo5&index=2

Backtesting a red-white-blue strategy
EMA = exponential moving average
6 short term EMA's in red and 6 longer term EMA's in blue
A quick way of identifying a short-term trend in an equity
The entry point is when the red first crosses the blue
And then when it breaks down is the sell signal
We have to enumerate these entries and exits in a way that Python can read/backtest
Use a for loop to iterate through each date and checks whether or not we're in a 
    red-white-blue pattern or a blue-white-red pattern

Crosses as indicators: https://www.investopedia.com/articles/technical/052201.asp

 - If the short-term moving average crosses below the longer-term moving average, you should short the stock.

 - If the short-term moving average crosses above the longer-term moving average, you should go long on the stock.

 According to Investopedia, "[a]n exponential moving average (EMA) is a type of moving average (MA) that places a greater weight and significance on the most recent data points. The exponential moving average is also referred to as the exponentially weighted moving average. An exponentially weighted moving average reacts more significantly to recent price changes than a simple moving average (SMA), which applies an equal weight to all observations in the period." https://www.investopedia.com/terms/e/ema.asp

 Use these EMAs with the same basic for-loop we've constructed to check every single date to see if we're in a red-white-blue pattern or a blue-white-red pattern. The program will simulate entering and exiting our positions based on the EMA pattern it finds. Then at the end it will print summary statistics that will help us measure how effective that strategy was. This is useful in determining if the strategy you're using is a good one or not.

THIRD VIDEO:
https://www.youtube.com/watch?v=hngHA9Jjbjc&list=PLPfme2mwsQ1FQhH1icKEfiYdLSUHE-Wo5&index=3

How to create dialog pop-up boxes that allow the user to select different files to manipulate. How to select stock market symbols. The program will look at the stocks listed on a spreadsheet and check each for 8 separate conditions outlined in Mark Minervini's book. These conditions indicate if a stock is ready to be bought and if it will go on a massive run. A good starting point to trading will help you pick stock on an overall uptrend. The progam will also write the output to another Excel sheet. Run this program with a whole bunch of stocks and pick out the ones that meet MM's strict investment criteria:

        #Condition 1: Current Price > 150 SMA and > 200 SMA
		#Condition 2: 150 SMA and > 200 SMA
		#Condition 3: 200 SMA trending up for at least 1 month (ideally 4-5 months)
		#Condition 4: 50 SMA> 150 SMA and 50 SMA> 200 SMA
		#Condition 5: Current Price > 50 SMA
		#Condition 6: Current Price is at least 30% above 52 week low (Many of the best are up 100-300% before coming out of consolidation)
		#Condition 7: Current Price is within 25% of 52 week high
		#Condition 8: IBD RS rating >70 and the higher the better

The program will first try to see if yahoo has data on a stock and then if so, we'll check to see if it meets these conditions. If it does, we'll add it to a list called exportList that saves to another Excel file.