## 스택 수열
'''
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

입력
첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

출력
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.


1부터 n까지에 수에 대해 차례로 [push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop] 연산을 수행하면 수열 [4, 3, 6, 8, 7, 5, 2, 1]을 얻을 수 있다.

입력 수열 1234(4push)-> 4pop ->  3pop -> 1256(2push) 6pop 2push 12578 8pop 7pop 5 2 1 pop
4push 2pop 2push 1pop 2push 5pop

출력 수열에 존재하는 숫자는 입력수열에 다시 가져가지 않는다는 생각?
출력 수열 입력수열의 4 가져옴, 3가져옴
[4,3,6,8,7,5,2,1]

예제 2 12534 -> 불가능 (543)이면 가능했지만 534 -> 34가 불가능.
13245->
max값은 n값과 동일하다.

42351 ->불가능하네? 모든 숫자에 대해서 차례대로 내려가거나 차례대로 올라가는 것만 가능.
stack 데이터 안에 li의 숫자가 없으면 하나씩 push를 넣는다.
만약 숫자가 있다면 data에 pop을 한다.

'''

import sys
import time
from collections import deque

start = time.time()
sys.stdin = open('solution/jlee14233/02. data_structure/입력.txt', 'r')

n=int(sys.stdin.readline())
li=[int(sys.stdin.readline()) for i in range(n)]

stack=[0]
out=[]
data=[]
flag=0
cur=1

for i in range(n):
    if li[i]!=stack[-1]:
        for j in range(0 if len(out)==0 else int(out.count('+')),li[i]+1):
            stack.append(j)
            out.append('+')
        data.append(stack.pop())
        out.append('-')
    else:
        data.append(stack.pop())
        out.append('-')
    
    if data[-1]!=li[:len(data)][-1]:
        flag=1
        print('NO')
        break

if flag==0: print(*out,sep='\n')

print("time :", time.time() - start) 
'''
time : 0.0010008811950683594ms
앞선 풀이가 틀린 것은 아니지만 시간 복잡도가 엄청 높았나 보다 O(N^2)까지도 될 정도의 복잡도를 갖고 있나봄.
for 밑의 for 문에서 변수를 지정하고 변수로 처리하는 방법을 선택해야 조금 더 빠른 속도로 문제를 해결 할 수 있다는 것을 기억해야 한다.
time : 0.022020578384399414
time : 0.02357339859008789

'''
sys.stdin = open('solution/jlee14233/02. data_structure/입력.txt', 'r')

n=int(sys.stdin.readline())

stack=[]
out=[]
data=[]
flag=0
cur=1

start = time.time()
for i in range(n):
    num=int(sys.stdin.readline())
    while cur <= num:
        stack.append(cur)
        out.append('+')
        cur+=1
    if stack[-1]==num:
        stack.pop()
        out.append('-')
    else:
        print('NO')
        flag=1
        break

if flag==0:
    print(*out,sep='\n')

print("time :", time.time() - start)