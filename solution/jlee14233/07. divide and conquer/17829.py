### 222-풀링
'''
문제
조기 졸업을 꿈꾸는 종욱이는 요즘 핫한 딥러닝을 공부하던 중, 이미지 처리에 흔히 쓰이는 합성곱 신경망(Convolutional Neural Network, CNN)의 풀링 연산에 영감을 받아 자신만의 풀링을 만들고 이를 222-풀링이라 부르기로 했다.

다음은 8×8 행렬이 주어졌다고 가정했을 때 222-풀링을 1회 적용하는 과정을 설명한 것이다

행렬을 2×2 정사각형으로 나눈다.

각 정사각형에서 2번째로 큰 수만 남긴다. 여기서 2번째로 큰 수란, 정사각형의 네 원소를 크기순으로 a4 ≤ a3 ≤ a2 ≤ a1 라 했을 때, 원소 a2를 뜻한다.

2번 과정에 의해 행렬의 크기가 줄어들게 된다.

종욱이는 N×N 행렬에 222-풀링을 반복해서 적용하여 크기를 1×1로 만들었을 때 어떤 값이 남아있을지 궁금해한다.

랩실 활동에 치여 삶이 사라진 종욱이를 애도하며 종욱이의 궁금증을 대신 해결해주자.

입력
첫째 줄에 N(2 ≤ N ≤ 1024)이 주어진다. N은 항상 2의 거듭제곱 꼴이다. (N=2K, 1 ≤ K ≤ 10)

다음 N개의 줄마다 각 행의 원소 N개가 차례대로 주어진다. 행렬의 모든 성분은 -10,000 이상 10,000 이하의 정수이다. 

'''


import sys
import math
import time
from collections import deque
sys.stdin = open('solution/jlee14233/07. divide and conquer/입력.txt', 'r')

n= int(sys.stdin.readline().strip())
mat=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]

queue=deque([])
operator=[]

def divide(graph,n):
    x=n//2
    a=[graph[_][:x] for _ in range(x)]
    b=[graph[_][x:] for _ in range(x)]
    c=[graph[x+_][:x] for _ in range(x)]
    d=[graph[x+_][x:] for _ in range(x)]

    return a,b,c,d

def oper(graph):
    a=sorted([_ for res in graph for _ in res])
    res=a[2]
    return res

def build(a,b,c,d):
    x=[[a,b],[c,d]]
    return x

queue.append(mat)
while queue:
    graph=queue.popleft()
    if len(graph)>2:
        a,b,c,d=divide(graph,len(graph))
        queue.append(a)
        queue.append(b)
        queue.append(c)
        queue.append(d)
    elif len(graph)==2:
        x=oper(graph)
        operator.append(x)
        if len(operator)==4:
            temp=build(*operator)
            queue.append(temp)
            operator=[]
print(operator[0])


'''
'''
import sys
input = sys.stdin.readline

def f(n, mat):
    if n == 2:
        li = []
        for i in range(2):
            for j in range(2):
                li.append(mat[i][j])
        li.sort()
        return li[2]
    else:
        temp = [[] for _ in range(n//2)]
        for i in range(0, n, 2):
            for j in range(0, n, 2):
                li = [mat[i][j], mat[i][j+1], mat[i+1][j], mat[i+1][j+1]]
                li.sort()
                temp[i//2].append(li[2])
        return f(n//2, temp)
## 이 부분 코드리뷰하면서 어떻게 재귀가 돌아가는지 다시한번 생각해보기.
## 내가 풀이한 방법은 너무 많은 리소스를 사용하는 것으로 밝혀짐. 시간도 많이 걸림 안좋은 코딩.

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

print(f(n, mat))