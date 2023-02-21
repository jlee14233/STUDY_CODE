## 트리의 부모 찾기

'''
문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
'''

import sys
from collections import deque

sys.stdin = open('solution/jlee14233/04. Graph/입력.txt', 'r')

n=int(sys.stdin.readline().strip())
# print(n)
ad_list = [[] for i in range(n+1)]
for i in range(n-1):
    
    a,b =map(int,sys.stdin.readline().strip().split())
    ad_list[a].append(b)
    ad_list[b].append(a)

def bfs(graph,start):
    visited=[False]*(n+1)
    queue=deque([start])
    visited[start]=True
    x=1
    while queue:
        v=queue.popleft()
        if x==2:
            sys.stdout.write(str(v)+'\n')
            break
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
        x+=1
    return visited
ans = [0]*(n+1)
queue=deque()
queue.append(1)
while queue:
    now = queue.popleft()
    for nxt in ad_list[now]:
        print(nxt,'nxt의 값')
        if ans[nxt] == 0:
            ans[nxt] = now           
            print(ans[nxt],'ans[nxt]')
            queue.append(nxt)
            print(queue)
            print(ans)
# for _ in range(2,n+1):
#     bfs(ad_list,_)
'''
위로 풀었을 때의 문제점. 다음 항을 계산하기 위해서 다시 반복하는 부분을 계속 해야함.
함수 자체를 돌려버린다는 개념이 시간초과를 유발하는 것 같음.
아래의 방식은 ans값을 그냥 저장해버려서 함수를 1번만 이용하게됨.
while문을 1번만 도는 것과
while문을 여러번 돌아야하는 것의 차이라고 볼 수 있음.
그렇다면 위의 식을 개조를 해서 ans값만 따로 모아두는 형식으로 바꾼다면?
시간초과를 막을 수 있다. 즉, return값을 ans값이 나오도록 형식을 바꿔버리면 된다.
아무리 x값을 1로 주고 1번만 돌도록 만들었어도? 그 부분이 무리를 주는 것이라고 생각함.


'''

N = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

ans = [0]*(N+1)

def bfs():
    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if ans[nxt] == 0:
                ans[nxt] = now
                queue.append(nxt)

bfs()
res=ans[:]
print(res)
for x in res:
    print(x)