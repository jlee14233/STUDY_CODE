## 효율적인 해킹
'''
문제
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.

이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.

이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

출력
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.

'''
import sys
from collections import deque
from collections import defaultdict
sys.stdin = open('solution/jlee14233/04. Graph/입력.txt', 'r')

n,m =map(int,sys.stdin.readline().strip().split())

ad_list = [[] for i in range(n+1)]
arr=set()
for i in range(m):
    
    a,b =map(int,sys.stdin.readline().strip().split())
    ad_list[b].append(a)
    arr.add(a)
    arr.add(b)

print(ad_list)

def bfs(graph,start):
    res=defaultdict(list)
    for _ in range(1,start+1):
        visited=[False]*(n+1)
        queue=deque([start])
        visited[start]=True
        cnt=0
        while queue:
            v=queue.popleft()
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i]=True
                    cnt+=1
        res[cnt].append(_) 

bfs(ad_list,n)

res=defaultdict(list)
for _ in range(1,n+1):
    visited=[False]*(n+1)
    queue=deque([_])
    visited[_]=True
    cnt=0
    while queue:
        v=queue.popleft()
        for i in ad_list[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                cnt+=1
    res[cnt].append(_)


def dfs(graph,v):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i)
    return visited
print(arr)
print(sorted(list(arr)))

res=defaultdict(list)
# print(sum(dfs(ad_list,10000)))
##여기에서 있는 숫자들만 선택하는 방법이 있을까?(set을 이용해서 복수를 줄인다.)
for _ in arr:
    visited=[False]*(n+1)
    res[sum(dfs(ad_list,_))].append(_)

print(*res.get(max(res.keys())))