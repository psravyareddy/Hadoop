#!/usr/bin/env python3
""" from operator import itemgetter
import sys
current_word=None
current_count=0
word=None
for line in sys.stdin:
    line=line.strip()
    word,count=line.split("\t",1)
    try:
        count=int(count)
    except ValueError:
        continue
    if current_word==word:
        current_count+=count
    else:
        if current_word:
            print("%s\t%s"%(current_word,current_count))
        current_count=count
        current_word=word
if current_word==word:
    print('%s\t%s'%(current_word,current_count))
"""
import sys
wc={}
for line in sys.stdin:
    line=line.strip()
    word,count=line.split("\t",1)
    try:
        count=int(count)
    except valueError:
        continue
    try:
        wc[word]=wc[word]+count
    except:
        wc[word]=count
for word in wc.keys():
    print("%s\t%s"%(word,wc[word]))

        


