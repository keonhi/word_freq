
# -*- coding: utf-8 -*-

def remove_puncts(string):
    output = ''
    for s in string:
        if s.isalnum():
            output = ''.join((output,s))
    return output

from collections import Counter
import sys

def get_counter(fname):
    
    words_counter = Counter()
    f = open(fname, 'r', encoding ='utf-8')
    for line in f:
        for word in line.lower().split():
            words_counter[remove_puncts(word)] += 1
    f.close()
    for word, freq in words_counter.most_common(10):
        print('{}\t{}'.format(word, freq))
        
fname = sys.argv[1]
get_counter(fname)