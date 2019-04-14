# word_freq


1~4.
(필수, 10점) 명령 매개변수로 텍스트 파일의 경로를 받아 단어 빈도를 계산하고 상위 10개 단어와 빈도를 출력하는 프로그램 word_freq.py를 작성하라.
(선택, +1점) 가능하면 아래의 내용을 추가해 보라.
• 파일 경로가 잘못 입력된 경우 ’<파일 경로>라는 파일이 없습니다.’라고 출력한다.
• 파일 경로가 입력되지 않은 경우 ’파일 경로를 입력하세요.’라고 출력한다.
(선택, +1점) 가능하면 아래의 내용을 추가해 보라.
• 두 개 이상의 파일 경로가 들어온 경우 모든 파일의 텍스트를 합쳐서 빈도를 계산한다.
• 잘못된 파일 경로가 섞여 있으면 존재하는 파일 경로에 대해서만 빈도를 계산한다.
(선택) 자신이 가지고 있는 hwp, doc 등의 문서를 txt로 저장하여 이 프로그램으로 빈도를 계산해
보라.
A.	문제 해결 방법
먼저 remove_puncts(string)라는 함수를 정의한다. 이 함수는 문자열을 문자 하나씩 읽으면서 글자나 숫자만 남긴다. 그리고 get_counter(fname)을 정의한다. 이 때 except를 사용해 예외처리를 한다. 지정한 파일이 없는 경우 다음과 같이 FileNotFoundError가 발생한다. 
 
이 경우 ‘<파일 경로>라는 파일이 없습니다.’라고 출력되도록 한다. 지정된 파일이 1개 이상 있는 경우는 파일을 하나씩 읽으면서 words_counter를 계산하고 total에 합쳐나간다.
만일 파일 경로가 지정되지 않은 경우는 ’파일 경로를 입력하세요.’라고 출력한다. 이 경우는 len(sys.arv)=1인 경우로 생각할 수 있다. 

B.	코드 설명
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

C.	테스트 실행 결과
 
