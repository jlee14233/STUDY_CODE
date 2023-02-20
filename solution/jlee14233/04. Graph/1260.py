## DFS와 BFS
'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
'''


import sys
from collections import deque

sys.stdin = open('solution/jlee14233/04. Graph/입력.txt', 'r')


N,e,v =map(int,sys.stdin.readline().strip().split())
ad_list = [[] for i in range(N)]
for i in range(e):
    a,b =map(int,sys.stdin.readline().strip().split())
    ad_list[a-1].append(b-1)
    ad_list[b-1].append(a-1)
ad_list=[sorted(i) for i in ad_list]
## 항마다 정렬을 해줘야했기 때문에 어쩔 수 없이 list comprehension으로 한번 더 처리해줌.
## 오름차순 정렬을 해야지 낮은 순번대로 돌기 떄문!

def dfs(graph,v,visited):
    visited[v]=True
    print(v+1, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
    return visited
    
def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v+1, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

    return visited

visited=[False]*N
dfs(ad_list,v-1,visited)
print()
visited=[False]*N
bfs(ad_list,v-1,visited)