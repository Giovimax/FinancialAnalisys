#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 13:18:22 2018

@author: giovimax
"""
#%%
import pandas as pd 

#%%
def intorfloat(string):
    try:
        toret = int(string)
        return toret
    except ValueError:
        return float(string)
    
#%%

def getFromAlpha(symbol, timeSeries = "TIME_SERIES_DAILY_ADJUSTED", start_time = None, end_time = None):
    """
    documentation at: https://www.alphavantage.co/documentation/
    """
    query = "https://www.alphavantage.co/query?"
    urlArg = str(query + "function=" + timeSeries + "&datatype=csv" + "&symbol=" + symbol + "&outputsize=full" + "&apikey=9126VWZ7ZVHJEJZ4")
    df = pd.read_csv(urlArg, index_col = "timestamp")
    col = list(df)#ottengo una lista delle colonne, più pratica
    #print(col)
    #reindexing
    df.index = df.index.map(pd.Timestamp)
    #df.sort_index()
    print(urlArg)
    for c in col:
        df[c] = df[c].apply(float)
    return df[end_time : start_time]#l'indicizzazione è al contrario, quando var=None non ci sono effetti collaterali
        

#%%
if __name__ == "__main__":   
    spy = getFromAlpha("SPY")

