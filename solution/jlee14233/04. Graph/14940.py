## 쉬운 최단거리

'''
문제
지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.

문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.

입력
지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)

다음 n개의 줄에 m개의 숫자가 주어진다. 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다. 입력에서 2는 단 한개이다.

출력
각 지점에서 목표지점까지의 거리를 출력한다. 원래 갈 수 없는 땅인 위치는 0을 출력하고, 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.

'''

import sys
from collections import deque
from collections import defaultdict


sys.stdin = open('solution/jlee14233/04. Graph/입력.txt', 'r')
n,m =map(int,sys.stdin.readline().strip().split()) ## y =n x=m
visited=deque([0 for _ in range(m)] for _ in range(n))
result=deque([0 for _ in range(m)] for _ in range(n))

# print(visited)

# a=[list(map(int,sys.stdin.readline().strip().split())) for i in range(n)] 
## 여기 부분을 풀어서 만든다면 2를 빠르게 찾을 수 있지 않을까?
a=[]
for i in range(n):
    num=list(map(int,sys.stdin.readline().strip().split()))
    if 2 in num:
        x=num.index(2)
        y=i
    a.append(num)

dx=[1,-1,0,0]
dy=[0,0,1,-1]

'''
아이디어 = 2의위치를 가장 처음 읽어야 한다.
2는 1번만 존재하기 때문에 2의 위치가 어디 있는지 찾는 것이 중요할 것이라고 생각된다.
    위의 list comprehension을 풀어서 x,y값을 구해냈다.

defaultldict을 이용하여 일단 정리를 append를 할 수 있도록 만든다.
밑의 함수를 이용하게 되면 좌표값과 최단거리를 구하는 함수이다.
node에는 x,y,최단거리가 출력이 되는데, 이 때 최단거리가 아닐 때에도 모든 값을 구하도록 만들어야 한다.
즉, 최단거리가 아닌 모든 거리를 출력시켜야하는 것이 중요하다.

'''
visited[y][x]=True

stack = deque([[x,y,0]]) ## x의 위치, y의 위치, 0은 cnt값

stack_1=deque([])## 0인 부분을 출력하기 위한 stack 
while stack:
    node = stack.popleft()
    result[node[1]][node[0]]=node[2]  ## 여기 부분 y값 들어가야하는 좌표계, 일반적으로 쓰는 좌표계를 계속 생각해야한다.
    for i in range(4):
        xx = dx[i] + node[0] # y축 이동
        yy = dy[i] + node[1] # x축 이동
        if 0<=xx<m and 0<=yy<n and not visited[yy][xx]:
            if a[yy][xx] == 1:
                visited[yy][xx] = True
                stack.append([xx,yy,node[2]+1])
            else:
                stack_1.append([xx,yy,a[yy][xx]])

while stack_1:
    node=stack_1.popleft()
    if node[2]==1:
        result[node[1]][node[0]]=-1
    for i in range(4):
        xx = dx[i] + node[0] # y축 이동
        yy = dy[i] + node[1] # x축 이동
        if 0<=xx<m and 0<=yy<n and not visited[yy][xx]:
            if a[yy][xx]==0:
                visited[yy][xx] = True
                stack_1.append([xx,yy,a[yy][xx]])
            else:
                visited[yy][xx] = True
                stack_1.append([xx,yy,a[yy][xx]])
for _ in result:
    print(*_)
'''
시간을 반으로 줄이고 싶으면 while문을 1개만 쓰도록 만들어버리면 된다.
지금은 최단경로를 계산하는 부분과 0이 존재할 때 섬이면 -1를 출력하는 부분을 따로 계산하도록 만들어버렸다.
이 부분을 어떻게 해결할 것인지 생각을 해서 결론을 한번에 짓도록 만들면 시간이 반으로 줄을 것이라고 생각한다.

후처리를 해야하는 부분 = visited에서 0000/0000/0000 가 발생한 부분은 
-1 로 변경해줘야한다.
그렇다면 위의 부분에서 stack_1 내용물의 최소값에 +1 +1 좌표를 입력해서 위에 다시한번 돌려준다는 생각을 한다.
bfs_minus 로 함수를 정해두면 될 거 같다.

'''
# print(stack,stack_1,visited)
# print(min(stack_1))