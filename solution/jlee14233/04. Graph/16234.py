## 인구 이동
'''
N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.

오늘부터 인구 이동이 시작되는 날이다.

인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
연합을 해체하고, 모든 국경선을 닫는다.
각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)

둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)

인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.

출력
인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.

10 5
5 25

0,0은 해당사항이 없다
1,0 0,1을 stack값에 추가함.
1,0부터 꺼내는데, visited가 안된 지역을 돈다
25는 해당사항이 있는 값이므로.
sum+=graph[yy][xx]
거기에 visited[yy][xx]=True로 변경한다.

'''

import sys
from collections import deque

sys.stdin = open('solution/jlee14233/04. Graph/입력.txt', 'r')

n,l,r=map(int,sys.stdin.readline().strip().split())
graph=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,-1,1]

# while문으로 처리를 해야하는 데, 무엇을 기준으로 해야하나?
# 모든 상황을 계속 봐야함.
# 그렇다면 그래프에서 다이나믹 프로그래밍을 쓰는게 맞지 않나?
# sum값을 어떻게 리셋할 것인지를 생각해야함. 뚫려 있다면 sum값을 리셋하지 않는 방향으로 해야하는 건데, 그 방향을 모르겠음.

def bfs(x,y):
    global move
    stack = deque([[x,y]])
    cont = 1
    temp =deque([[x,y]])
    Sum= graph[y][x]
    visited[y][x]=True
    while stack:
        node = stack.popleft()
        for i in range(4):
            yy = dy[i] + node[1] # y축 이동
            xx = dx[i] + node[0] # x축 이동
            if 0<=xx<n and 0<=yy<n and l<=abs(graph[node[1]][node[0]]-graph[yy][xx])<=r and not visited[yy][xx]:
                visited[yy][xx]=True
                stack.append([xx,yy])
                Sum+=graph[yy][xx]
                cont+=1
                temp.append([xx,yy])

    peo= Sum//cont

    if cont>1:
        move = True
        for x,y in temp:
            graph[y][x]=peo
    # return visited, count, Sum

days=0

while True:
    move = False
    visited=[[False]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if visited[y][x] is False:
                bfs(x,y)
    if move is True:
        days+=1
    else:
        break

    
print(days)
print(graph)
