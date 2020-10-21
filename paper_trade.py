#import functions
from functions import *
if len(sys.argv)>1:
    word = str(sys.argv[1:])
    # to reinitiate the paper trading system
    if (word == "['restart']"):
        b = float(input('what balance would you like to begin with?'))
        pf = [{'Date':str(dt.datetime.today().date()),'Balance':b,'Price':0.00,'Qty':0,'Stock':'NA'}]
        pf = pd.DataFrame(pf)
        pf.to_pickle('portfolio.pkl')
        print('reinitiated')
    else:
        print('please type restart if you wish to reinitiate.')

else:
    # the paper trading system
    x = input('the stock symbol as per yahoo_finance:') # the stock 
    q = int(input('units:')) # the quantity
    t = int(input ('1 = Buy, 0 = sell:')) # trade
    p = price_gen(x) # the price as per the current date

    pf = pd.read_pickle('portfolio.pkl')
    pd.set_option('display.max_columns',5)
    print(pf) # prints the portfolio

    pf = trade(pf,p,q,x,t)# executes the trade and appends the pf
    pf.to_pickle('portfolio.pkl') # store 

    print('The trade has been executed.')
