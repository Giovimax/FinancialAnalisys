#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 15:54:42 2018

@author: giovimax
"""

#%%
"""module cell
"""
import pandas as pd
import requests as re
import json
from matplotlib import pyplot as plt
from matplotlib import finance
import numpy as np

#%%
"""const
"""
Key = "9126VWZ7ZVHJEJZ4"
querry = "https://www.alphavantage.co/query?"
test = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=demo"

#%%
"""data preparation
"""
jd = json.loads(re.get(test).text)#dictionary from remote
selected_jd = jd[list(jd)[1]]#subselection of the data whithout meta
df = pd.DataFrame(selected_jd)#dataframe creation
df = df.transpose()#correcting index
col = list(df)#ottengo una lista delle colonne, più pratica
print(col)
#reindexing
df.index = df.index.map(pd.Timestamp)
for c in col[:-1]: #converto le quantità da str a float
    df[c] = df[c].apply(float)
df[col[-1]] = df[col[-1]].apply(int)


#%%
"""
for i in col:
    plt.plot(list(df.index), i, data = df)
plt.xlabel("DateTime")
plt.ylabel("Price")
plt.legend()
plt.xticks(rotation=45)
"""
#%%
"""
ax1 = plt.subplot(2,1,1)
plt.plot(df.index, col[0],"r", data=df)
plt.xticks(rotation=45)


ax2= plt.subplot(2,1,2, sharex = ax1)
plt.bar(df.index, col[4], data=df)
plt.xticks(rotation=45)

"""
