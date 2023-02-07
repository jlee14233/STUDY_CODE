## 덱

'''
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

import sys
from collections import deque

sys.stdin = open('solution/jlee14233/02. data_structure/입력.txt', 'r')

n= int(sys.stdin.readline())

dq=deque()
for i in range(n):
    i=sys.stdin.readline().split()
    if i[0]=='push_front':
        dq.appendleft(int(i[1]))
    elif i[0]=='push_back':
        dq.append(int(i[1]))    
    elif i[0]=='pop_front':
        if len(dq)==0:
            print(-1)
        else: 
            print(dq.popleft())
    elif i[0]=='pop_back':
        if len(dq)==0:
            print(-1)
        else: 
            print(dq.pop())
    elif i[0]=='size':
        print(len(dq))
    elif i[0]=='empty':
        if len(dq)==0:
            print(1)
        else: print(0)
    elif i[0]=='front':
        if len(dq)==0:
            print(-1)
        else: print(dq[0])
    elif i[0]=='back':
        if len(dq)==0:
            print(-1)
        else: print(dq[-1])