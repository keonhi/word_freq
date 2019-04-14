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
    total = Counter()
    for i in range(1,len(sys.argv)):
        try:
            fname = sys.argv[i]
            words_counter = Counter()
            f = open(fname, 'r', encoding ='utf-8')
            for line in f:
                for word in line.lower().split():
                    words_counter[remove_puncts(word)] += 1
            f.close()
            total += words_counter
        except FileNotFoundError:
            print("{}라는 파일이 없습니다.".format(fname))
    for word, freq in total.most_common(10):
            print('{}\t{}'.format(word, freq))

if len(sys.argv) > 1:
    fname = ''
    get_counter(fname)

else:
    print("파일 경로를 입력하세요.")