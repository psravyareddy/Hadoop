#!/usr/bin/env python3
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
sortedorder=sorted(wc.items(),key=lambda x:x[1],reverse=True)
for w in sortedorder[:10]:
    print('{}\t{}'.format(w[0],w[1]))

