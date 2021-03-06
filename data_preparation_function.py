#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 20:17:26 2018

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
def prepare(fileName):
    with open(filename,"br") as file:
        df = pickle.load(file)  
    
    df["raw_datetime"] = df["<DTYYYYMMDD>"] + df["<TIME>"]
    df["Timestamp index"] = df["raw_datetime"].apply(pd.to_datetime, format="%Y%m%d%H%M%S")
    
    del df["<TICKER>"]
    del df["<DTYYYYMMDD>"]
    del df["<VOL>"]
    del df["<TIME>"]
    del df["raw_datetime"]
    
    df = df.set_index("Timestamp index")
    
    
    #finalmente salvo e finisco con questa merda
    newFileName = filename.split(".")[0] + "_dataframe.txt"
    with open(newFileName, "ba") as file:
        pickle.dump(df, file)
        