#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 17:23:47 2018

@author: giovimax
"""

#followung tutorial at https://ntguardian.wordpress.com/2018/07/17/stock-data-analysis-python-v2/
#%%
"""modules
"""
import pandas as pd
import datetime
import quandl
import matplotlib.pyplot as plt
import numpy as np
import AlphaVantageUtilities as avu

#%%
"""variables/const
"""

start = datetime.date(2016,1,1)
end = datetime.date(2018,3,27)
a = "AAPL"
w = "WIKI/"

apple = quandl.get(w+a, start_date=start, end_date = end)
microsoft, google = (quandl.get("WIKI/" + s, start_date=start, end_date=end) for s in ["MSFT", "GOOG"])

#%%
#creo un df che contiene unicamente gli adj close degli stock per controllarli
stocks = pd.DataFrame({"APLL" : apple["Adj. Close"],
                      "MSFT" : microsoft["Adj. Close"],
                      "GOOG" : google["Adj. Close"],
                      "SPY" : avu.getFromAlpha("SPY", end_time=end, start_time=start)["adjusted_close"]})

stocks.plot(grid = True, secondary_y=["GOOG"])#plotta gli stock, assi separati

#%%
#analisi del cambio relativo degli stock
stocks_return = stocks.apply(lambda x: x/x[0])#rendimento da start
stocks_return_relative = stocks.apply(lambda x: x/x.shift(1))#rendimento
stocks_return_log = stocks.apply(lambda x: np.log(x)-np.log(x.shift(1)))
stocks_return_log_relative = stocks.apply(lambda x: np.log(x)-np.log(x[0]))
stocks_change_apr = stocks_return_log.apply(lambda x: x*252*100)

#%%
tbill =quandl.get("WIKI/" + "FRED/TB3MS" , start_date=start, end_date=end)["Adj. Close"]

#%%
#creo varie ma così da poterle confrontare
apple["20d"] = np.round(apple["Adj. Close"].rolling(20).mean(),2)
apple["50d"] = np.round(apple["Adj. Close"].rolling(50).mean(),2)
apple["5d"] = np.round(apple["Adj. Close"].rolling(5).mean(),2)
apple_i = apple.loc[:,["Adj. Close", "5d", "20d", "50d"]]#creo un df con solo i dati interessanti da plottare
#creo due tipi di Mooving Average per ogni stock in stocks
for col in list(stocks):
    for n in [20,50]:
        stocks["{}d ma {}".format(n,col)] = np.round(stocks[col].rolling(n).mean(),2)

#%%
#inizio a pensare a una strategia ultra basilare di trading e la metto in pratica
#utilizzerò principalmente lo stock apple
apple["20d-50d"] = apple["20d"] - apple["50d"]
"""plotting per confermare la funzionalità
plt_index = apple.index
ax1 = plt.subplot(2,1,1)
plt.plot(apple_i)
ax2 = plt.subplot(2,1,2, sharex = ax1)
plt.plot(apple["20d-50d"])
"""
apple["Regime"] = [1.0 if x >= 0 else -1.0 for x in apple["20d-50d"]]
#apple["Action"] = ["Sell" if a ==1 & b == -1 "Buy" elif a==-1 & b==1 for a,b in zip(apple["Regime"),apple["Regime"].shift(1)]
conditions = [(apple["Regime"]== 1) & (apple["Regime"].shift(1) == -1),
              (apple["Regime"]== -1) & (apple["Regime"].shift(1) == 1)]
choices = [1, -1]
apple["Action"] =  np.select(conditions, choices, default = 0)
#il plotting rivela che funziona tutto, ora va creato il sistema di back testing






