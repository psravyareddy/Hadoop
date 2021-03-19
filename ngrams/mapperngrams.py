#!/usr/bin/env python3
import sys
import re
for eachline in sys.stdin:
    eachline=eachline.strip()
    pat=re.compile(r'[^a-zA-Z ]+')
    sentence=re.sub(pat,'',eachline)
    wordsineachline=sentence.split()
    numwords=len(wordsineachline)
    for index,word in enumerate(wordsineachline[:numwords-2]):
        word1=wordsineachline[index]
        word2=wordsineachline[index+1]
        word3=wordsineachline[index+2]
        if word1=='science' or word1=='sea' or word1=='fire':
            word1='$'
        elif word2=='science' or word2=='sea' or word2=='fire':
            word2='$'
        elif word3=='science' or word3=='sea' or word3=='fire':
            word3='$'
        if word1.find('$')!=-1 or word2.find('$')!=-1 or word3.find('$')!=-1:              print('{}_{}_{}\t{}'.format(word1,word2,word3,1))



