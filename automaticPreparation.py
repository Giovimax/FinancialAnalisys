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

toSkip = []

if "log.txt" in os.listdir(pathName):
    with open("log.txt","r+") as log:
        line = log.readline()
        while line:
            print("Read %s, set to be skipped" % line)
            toSkip.append(line.split())
            


log = open("log.txt","a+")
start = copy(datetime.datetime.now())
print("Starting the process...","time:",start)

for file in os.listdir(pathName):
    if file in toSkip:
        print("Skipping %s" %file)
        pass
    else:
        print("preparing:", file)
        print("Time:", datetime.datetime.now())
        dpf.prepare()
        print("done")
finish = datetime.datetime.now()
print("Process finished at:", finish)
print("timedelta= {}".format(datetime.timedelta(start,finish)))
log.close()