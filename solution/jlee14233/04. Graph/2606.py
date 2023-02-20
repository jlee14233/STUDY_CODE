## 바이러스
'''
문제
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

출력
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
'''


import sys
from collections import deque

sys.stdin = open('solution/jlee14233/04. Graph/입력.txt', 'r')

cpu=int(sys.stdin.readline().strip())
edge=int(sys.stdin.readline().strip())
node=deque([0 for _ in range(cpu)] for _ in range(cpu))
ad_list = [[] for i in range(cpu)]

for i in range(edge):
    a,b =map(int,sys.stdin.readline().strip().split())
    node[a-1][b-1]=1
    node[b-1][a-1]=1
    ad_list[a-1].append(b-1)
    ad_list[b-1].append(a-1)

def dfs(graph,v,visited):
    visited[v]=True
    # print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
    return visited
    
def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        # print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

    return visited

visited=[False]*cpu
print(bfs(ad_list,0,visited))
print(sum(visited)-1)

visited=[False]*cpu
dfs(ad_list,0,visited)
print(sum(visited)-1)
print(visited)
### visited의 수를 이용해서 풀이를 한다. 연결된 것만 True로 반환하기 때문에, True의 수만 센 후 (sum) 처음 정점인 1을 빼준다.



