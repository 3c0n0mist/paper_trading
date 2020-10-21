# import the libraries
import pandas as pd
import numpy as np
from pandas_datareader.yahoo.quotes import YahooQuotesReader
import datetime as dt
import sys

# the functions
def price_gen(x):
    """
    takes a stock symbol as presented in yahoo finance and extracts the price.
    """
    p = YahooQuotesReader(x).read()['price']
    return float(p)


def trade(pf,p,q,x,t):
    """
    a buy algortihm to record buy qty and price.
    t is a flag indicator for buy or sell, 1 buy and 0 sell 
    """

    if len(pf) == 1:
        b = float(pf['Balance'])
    else:
        b = float(pf['Balance'].tail(1))

    # if t = 1, means buy        
    if t > 0 :
        b = b - p*q
        print(f'bought {q} units of {x} at price {p}, remaining balance is {b}')
    else:
        b = b + p*q
        print(f'sold {q} units of {x} at price {p}, remaining balance is {b}')
    
    pf = pf.append({'Date':str(dt.datetime.today().date()),'Balance':b,'Price':p,'Qty':q,'Stock':x},ignore_index=True)
    print('appended to pf')
    return(pf)
