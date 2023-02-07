##괄호

'''
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

첫번째 빠르게 제외하는 방법
(=a )=b라고 했을 때 abab는 vps aba는 vps가 아니다.
첫번째로 전체의 개수가 홀수인지 아닌지를 선별하고 홀수이면 no를 출력한다.
a와 b를 설정하고, a와 b의 개수를 세서 같지 않을 경우 no를 출력한다.
abbaab같은 경우가 발생하였을 때 해결이 필요.
aabbabba
(()())((()))
aababbaaabbb
popleft로 하나씩 뺄 때 
a이면 +1
b이면 -1
a+b>=0 일 경우에만 식이 성립하게 됨.
++-- 
abbbaa
()))((
++--+--
++++-+--+-
++-+--+++---
+_+_+_+_++_+_+__+_

())(

'''

import sys
from collections import deque

sys.stdin = open('solution/jlee14233/02. data_structure/입력.txt', 'r')

n= int(sys.stdin.readline())

for i in range(n):
    dq=deque(sys.stdin.readline().rstrip())
    # print(i)
    # print(len(i))
    if len(dq)%2!=0: 
        print('NO')
    else:
        l,r=0,0
        count=set()
        while len(dq)!=0:
            if dq.popleft()=='(':
                l+=1
            else:
                r+=1
            k=l-r
            count.add(k)
        # print(dq,l,r,count)
        if l!=r or -1 in count:
            print('NO')
        else:
            print('YES')

'''
n = int(input())

for _ in range(n):
    words = input()

    while '()' in words:
        words = words.replace('()', '')

    if len(words):
        print('NO')
    else:
        print('YES')
'''