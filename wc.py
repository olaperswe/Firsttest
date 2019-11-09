# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:11:39 2019

@author: Ola
"""

stopwords_eng=["the","and","to","in","of", "from","on","for","as","by","at"]
stopwords_swe=["att", "är", "och","en","det","som","ett","detta","inte","på",
          "med","om","de","jag","den","av","till","för","eller","för",
          "man","han","men","så","då","ni","har","ska","vi","i"]

def filetodict(fp,di,stopwords) :
   """Read a file and populate dictionary with the words, exclude stopwords """
   for line in fp :
#    line=line.rstrip()
    wds=line.split()
    for w in wds:
        if w not in stopwords:
            if w in di:
                di[w]=di[w]+1
            else:
                di[w] = 1 

filename=input("Filename:")
fp=open(filename)
if fp != 0:
    di=dict()
    filetodict(fp,di,stopwords_swe)
    sortedByNumberDict = sorted(di.items(),key=lambda t:t[1])
    n=min(len(sortedByNumberDict),5)
    print (sortedByNumberDict[-n:])
