# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:11:39 2019

@author: Ola
"""

filename=input("Filename:")

fp=open(filename)

di=dict()

for line in fp :
    line=line.rstrip()
    wds=line.split()
    for w in wds:
        if w in di:
            di[w]=di[w]+1
        else:
            di[w] = 1

sortedByNumberDict = sorted(di.items(),key=lambda t:t[1])

print (sortedByNumberDict)