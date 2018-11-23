#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 19:08:51 2018

@author: giovimax
"""

import os
import data_preparation_function as dpf
import datetime
from copy import copy

pathName = ""
start = copy(datetime.datetime.now())
print("Starting the process...","time:",start)

for file in os.listdir(pathName):
    print("preparing:", file)
    print("Time:", datetime.datetime.now())
    dpf.prepare()
    print("done")

print("Process finished at:", datetime.datetime.now())