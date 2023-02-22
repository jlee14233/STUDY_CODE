## 미로 찾기 -- 연습문제
#다른 사람의 코딩을 보고 익히기! 가중치가 없는 그래프에서의 최단경로 구하기 문제.

'''
문제
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

'''
import sys
from collections import deque

sys.stdin = open('solution/jlee14233/04. Graph/입력.txt', 'r')
n,m =map(int,sys.stdin.readline().strip().split())
visited=deque([0 for _ in range(m)] for _ in range(n))

print(visited)

a=[list(map(int,sys.stdin.readline().strip())) for i in range(n)] 
print(a)

dx=[1,-1,0,0]
dy=[0,0,1,-1]

visited[0][0]=True
stack = deque([[0,0,1]]) ## x의 위치, y의 위치, 1은 cnt값
while stack:
    node = stack.popleft()
    # print(node)
    if node[0] == n-1 and node[1] == m -1: ## 마지막 위치에 왔을 때의 도착한 거리? 최단거리?
       print(node[2]) 
    for i in range(4):
        xx = dx[i] + node[0] # y축 이동
        yy = dy[i] + node[1] # x축 이동
        if 0<=xx<n and 0<=yy<m and not visited[xx][yy] and a[xx][yy] == 1:
            visited[xx][yy] = True
            stack.append([xx,yy,node[2]+1])
            # print(visited)
