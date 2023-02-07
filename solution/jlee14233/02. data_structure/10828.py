## 스택

'''
 stack
 FILO의 구조를 띄는 자료구조, 삽입과 삭제 연산이 동일한 한군데에서 발생함.
 삽입/삭제 연산에 있어 시간복잡도가  O(1)이다.
 이전에 활용한 데이터를 역으로 추적하거나, 처음에 들어온 데이터 보다 나중에 들어온 데이터가 빨리 나가야 할 때 사용.
 python에서는 list의 pop 기능을 활용하면 stack과 같이 사용이 가능함.

'''

import sys

sys.stdin = open('solution/jlee14233/02. data_structure/입력.txt', 'r')

n= int(sys.stdin.readline())
# def Stack(list,x):
#     if x[0]=='push':
#         list.append(int(x[1]))
#         pass

#     if x[0]=='pop':
#         if len(list)==0:
#             return -1
#         else:
#             return list.pop()

#     if x[0]=='size':
#         return len(list)
    
#     if x[0]=='empty':
#         if len(list)==0:
#             return 1
#         else:
#             return 0
    
#     if x[0]=='top':
#         if len(list)==0:
#             return -1
#         else:
#             return list[-1]


stack=[]

for i in range(n):
    i=sys.stdin.readline().rstrip().split()

    if i[0]=='push':
        stack.append(int(i[1]))
        
    if i[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())

    if i[0]=='size':
        print(len(stack))
    
    if i[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    
    if i[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
