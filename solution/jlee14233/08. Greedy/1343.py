##폴리오미노
'''
문제
민식이는 다음과 같은 폴리오미노 2개를 무한개만큼 가지고 있다. AAAA와 BB

이제 '.'와 'X'로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다. 이때, '.'는 폴리오미노로 덮으면 안 된다.

폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 보드판이 주어진다. 보드판의 크기는 최대 50이다.

출력
첫째 줄에 사전순으로 가장 앞서는 답을 출력한다. 만약 덮을 수 없으면 -1을 출력한다.
'''

import sys
from collections import deque

sys.stdin = open('solution/jlee14233/08. Greedy/입력.txt', 'r')

def trans(x):
    res=[]
    while x:
        i=deque.popleft(x)
        if len(i)%2==1:
            print(-1)
            quit()
        if len(i)%2==0:
            j=len(i)//4
            k=len(i)%4
            if len(x)!=0:
                if k==0 and j>=1:
                    temp=i[:j*4].replace('X','A')
                else:
                    temp=i[:j*4].replace('X','A')+i[-2:].replace('X','B')
                res.append(temp)
            else:
                if k==0 and j>=1:
                    temp=i[:j*4].replace('X','A')
                else:
                    temp=i[:j*4].replace('X','A')+i[-2:].replace('X','B')
                res.append(temp)
        elif i=='':
            res.append('.')
    return res


# x=deque(map(str,sys.stdin.readline().strip().split('.')))
# print(x)
# print(".".join(trans(x)))

n=str(sys.stdin.readline())

n=n.replace('XXXX','AAAA')
print(n)
n=n.replace('XX','BB')
print(n)
if 'X' in n:
    n  = '-1'

print(n)
