##큐

'''
 Quene
 FIFO 구조를 띄는 자료구조, 삽입과 삭제 연산이 서로 다른 한군데에서 발생한다.
 삽입/삭제 연산에 있어 시간복잡도는 O(1)이다.
 맨 앞을 front, 맨 뒤를 rear이라고 하고, 삽입 연산은 enqueue 삭제연산을 dequeue라고 한다.
 순차적으로 진행되어야 하는 일을 스케쥴링 할 때 사용된다.

 python에서는 queue를 import해서 사용할 수 있다

 Deque
 Queue/Stack 구조를 합친 구조로, 양쪽에서 삽입과 삭제 모두 할 수 있다.
 삽입/삭제 연산에 있어 시간복잡도가 O(1)이다.
 iterable(지우거나 쓰는 것이 가능한)데이터를 기반으로 선언 가능하고, 왼쪽에서 진행하는 연산에는 left를 붙인다.
 Queue는 멀티 스레드 환경에 최적화 되었으며, Deque의 경우 속도 측면에서는 더 빠르다.
 코딩테스트 환경에서는 Deque을 쓰는 것을 권장함.


 from collections import deque로 불러들여서 사용.
 대부분의 연산이 list와 매우 유사하나, 앞에서 진행되는 연산은 left를 붙여서 사용한다.

'''
import sys
from collections import deque

sys.stdin = open('solution/jlee14233/02. data_structure/입력.txt', 'r')

n= int(sys.stdin.readline())

dq=deque()
for i in range(n):
    i=sys.stdin.readline().split()
    if i[0]=='push':
        dq.append(int(i[1]))
    elif i[0]=='pop':
        if len(dq)==0:
            print(-1)
        else: 
            print(dq.popleft())
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