#!/usr/bin/env python3
import sys
import re
pat=re.compile(r'[^a-zA-Z ]+')
for eachline in sys.stdin:
    eachline=eachline.strip()
    string=re.sub(pat,'',eachline)
    wordsineachline=string.split()
    for words in wordsineachline:
        print("%s\t%s"%(words,1))





