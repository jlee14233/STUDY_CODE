## 단지 번호 붙이기
'''
문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.



입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

'''

import sys
from collections import deque

sys.stdin = open('solution/jlee14233/04. Graph/입력.txt', 'r')

n =int(sys.stdin.readline().strip())
visited=[[0 for _ in range(n)] for _ in range(n)]

ad_mat=[list(map(int,sys.stdin.readline().strip())) for i in range(n)]

def  bfs(x,y):
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    queue = deque()
    queue.append((x,y))
    ad_mat[x][y] = 0   
    #visited를 채운다는 것이 아닌 지나온 경로는 0으로 바꿔버린다는 개념/ 1을 0으로 바꾸면서 다시 찾으면 0이기 때문에 카운트가 안된다는 것을 이용함. 지난 풀이에서는, visited라는 새로운 행렬에 지나온 길을 늘려가는 방식으로 찾았다면, 이번에는 내 주변에 단지들이 있을 때 1을 0으로 바꾸면서 단지의 수만 계산하기 위함으로 보임.
    cnt =1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            xx = x +dx[i]
            yy = y +dy[i]

            if 0<=xx<n and 0<=yy<n and ad_mat[xx][yy]==1: 
                ad_mat[xx][yy] =0
                queue.append((xx,yy))
                cnt+=1

    return cnt

cnt=[bfs(i,j) for i in range(n) for j in range(n) if ad_mat[i][j]==1]
print(len(cnt))
print(*sorted(cnt),sep='\n')

# print(bfs(0,1))
# print(visited)

'''
문제풀이 실패. 다른 사람의 코드를 리뷰하면서 어떤 방식으로 풀이가 진행되었는지 알아보기.
내가 실패한 유형 > 바로 밑의 테스트 코드에서 0만 나와서 실패함.
기존 풀이 방식

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

이 코드를 바꾸면서 풀이를 진행하였음.

10
1010101010
0101010101
1010101010
0101010101
1010101010
0101010101
1010101010
0101010101
1010101010
0101010101

'''