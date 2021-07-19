# Challenge-3-

## Explaination of Challenge and findings 

In challenge 3 we looked at the closing price of Bitcoin, during a specific period of time, on two different exchanges, Bitstamp and Coinbase. This data was stored on two CSVs

We took the data from those comma seperated values and turned them into dataframes, which we could further manipulate through Pandas.

We took slices of these dataframes to get a closer look at how the prices differed between the two exchanges during 3 seperate 1 month periods. This data was also described and plotted.

Armed with this information we looked to see what sort of arbitrage opportunites existed. 

By further manipulationing the slices we took we were able to drop the non number values, and determine which arbitrage opportunites would be greater than our cost to conduct them.

What was found was that early timeframe the potential for arbitrage profit was higher, but there were more total opportunites later in the time series. 

The cumulative profit for each slice was also taken and graphed. 

## Technologies  

This application is written in Python 3.7
with use of the Pathlib (https://docs.python.org/3/library/pathlib.html)
as well as Pandas (https://pandas.pydata.org)

and Matplotlib (https://matplotlib.org


## Installation 
Before running the application first install the following dependencies.

python
  pandas
  Pathlib
  Matplotlib 
  
  
  ## Contributors

Sean Patel (myself) seanpatel076@gmail.com
---

## License

License is public anyone can use or make changes to this application
