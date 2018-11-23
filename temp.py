#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 20:22:55 2018

@author: giovimax
"""
#%%
#imports
import pandas as pd
import pickle
from copy import copy
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

#%%
#code
"""
with open("pick_copy_2.txt","br") as file:
    df = pickle.load(file)
    pass
"""
#%%
"""
df_c = copy(df)


for index, row in df_c.iterrows():
    df_c[index,"raw_datetime"] = a(row["<DTYYYYMMDD>"],row["<TIME>"])

"""
#%%
def converter(time):
    """storia triste:
       sembra pandas.read_csv  trasformi ogni item nel data tipe più congeniale,
       dunque questo formato di date viene trasformato in int64
       caso vuole però che un questo caso gli zeri all'inizio dell'item in
       questa circostanza siano più che cosmetici quindi ora mi tocca rimetterli
    """
    time = str(time)
    l = len(time)
    if l == 6:
        return pd.to_datetime(time,format=('%H%M%S'))
    elif l == 5:
        time = "0" + time
        return pd.to_datetime(time,format=('%H%M%S'))
    elif l == 4:
        return pd.to_datetime(time,format=('%M%S'))
    elif l == 3:
        time = "0" + time
        return pd.to_datetime(time,format=('%M%S'))
    elif l == 2:
        return pd.to_datetime(time,format=('%S'))
    elif l == 1:
        time = "0" + time
        return pd.to_datetime(time,format=('%S'))
    else:
        print(time, "errore")
        raise ValueError
#%%
"""
convertiti i formati 
print("start",dt.datetime.now())
df_c["date"] = df_c["<DTYYYYMMDD>"].apply(pd.to_datetime, format="%Y%M%d")

test performance, dovrebbe impiegare circa 6,50 min
%timeit df_c["<DTYYYYMMDD>"][:100000].apply(pd.to_datetime, format="%Y%M%d")
6.55 s ± 156 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)



df_c["time"] = df_c.loc[:,["<TIME>"]].apply(lambda x: x.apply(converter))
#df_c.loc[:10,["<TIME>"]].apply(lambda x: x.apply(converter))
with open("pick_copy_2.txt","ba") as file:
    pickle.dump(df_c,file)

print("finish",dt.datetime.now())
ho cronometrato la durata 
start 2018-10-12 00:38:56.741289
finish 2018-10-12 00:59:16.939512

#%%
#parte sperimentale
df_c["DateTime Index"] = (df_c["date"],df_c["time"])

#%%
#sperimentazione sulla fusione del tempo
df_small = df_c[:10]
df_small["date"] = df_small["<DTYYYYMMDD>"].apply(pd.to_datetime, format="%Y%M%d")
df_small["time"] = df_small.loc[:,["<TIME>"]].apply(lambda x: x.apply(converter))
#df_small["DateTime Index"] = (df_small["date"],df_small["time"])

def todatetime(timestamp):
    return timestamp.to_pydatetime
temp_datetime = []
df_small["datetime_index"] = df.apply(lambda r: pd.datetime.combine(r["date"],r["time"]),1)
    
"""
#%%






