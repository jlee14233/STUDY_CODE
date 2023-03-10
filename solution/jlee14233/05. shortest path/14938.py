##서강그라운드
'''
문제
예은이는 요즘 가장 인기가 있는 게임 서강그라운드를 즐기고 있다. 서강그라운드는 여러 지역중 하나의 지역에 낙하산을 타고 낙하하여, 그 지역에 떨어져 있는 아이템들을 이용해 서바이벌을 하는 게임이다. 서강그라운드에서 1등을 하면 보상으로 치킨을 주는데, 예은이는 단 한번도 치킨을 먹을 수가 없었다. 자신이 치킨을 못 먹는 이유는 실력 때문이 아니라 아이템 운이 없어서라고 생각한 예은이는 낙하산에서 떨어질 때 각 지역에 아이템 들이 몇 개 있는지 알려주는 프로그램을 개발을 하였지만 어디로 낙하해야 자신의 수색 범위 내에서 가장 많은 아이템을 얻을 수 있는지 알 수 없었다.

각 지역은 일정한 길이 l (1 ≤ l ≤ 15)의 길로 다른 지역과 연결되어 있고 이 길은 양방향 통행이 가능하다. 예은이는 낙하한 지역을 중심으로 거리가 수색 범위 m (1 ≤ m ≤ 15) 이내의 모든 지역의 아이템을 습득 가능하다고 할 때, 예은이가 얻을 수 있는 아이템의 최대 개수를 알려주자.



주어진 필드가 위의 그림과 같고, 예은이의 수색범위가 4라고 하자. ( 원 밖의 숫자는 지역 번호, 안의 숫자는 아이템 수, 선 위의 숫자는 거리를 의미한다) 예은이가 2번 지역에 떨어지게 되면 1번,2번(자기 지역), 3번, 5번 지역에 도달할 수 있다. (4번 지역의 경우 가는 거리가 3 + 5 = 8 > 4(수색범위) 이므로 4번 지역의 아이템을 얻을 수 없다.) 이렇게 되면 예은이는 23개의 아이템을 얻을 수 있고, 이는 위의 필드에서 예은이가 얻을 수 있는 아이템의 최대 개수이다.

입력
첫째 줄에는 지역의 개수 n (1 ≤ n ≤ 100)과 예은이의 수색범위 m (1 ≤ m ≤ 15), 길의 개수 r (1 ≤ r ≤ 100)이 주어진다.

둘째 줄에는 n개의 숫자가 차례대로  각 구역에 있는 아이템의 수 t (1 ≤ t ≤ 30)를 알려준다.

세 번째 줄부터 r+2번째 줄 까지 길 양 끝에 존재하는 지역의 번호 a, b, 그리고 길의 길이 l (1 ≤ l ≤ 15)가 주어진다.

출력
예은이가 얻을 수 있는 최대 아이템 개수를 출력한다.
'''

import sys
from collections import deque
import heapq
from collections import defaultdict

sys.stdin = open('solution/jlee14233/05. shortest path/입력.txt', 'r')

INF =int(1e9)

n,m,r =map(int,sys.stdin.readline().strip().split())
items=list(map(int,sys.stdin.readline().strip().split()))
graph=[[] for i in range(n+1)]
dis=[INF]*(n+1)
for _ in range(r):
    a,b,l=map(int,sys.stdin.readline().strip().split())
    graph[a].append((b,l))
    graph[b].append((a,l))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))  ## 시작점 거리는 0이고, start는 시작 점을 의미한다.  
    dis[start]=0 ## 거리 자기 자신은 0이다.
    ## heap자료구조상 앞의 거리 값이 낮은 것부터 노드를 검색하게 된다, 즉 2,2 가 들어가면 2가 가장 낮으므로 2번 노드를 탐색 하게 되고 그 이후 1,5 이런게 들어가있다면 5번 노드부터 탐색하게된다. 앞의 정보가 낮은 것부터 탐색하도록 만들고, 거리 값이 낮은 것을 기준으로 최단거리를 구하기 떄문에, 항상 최단거리를 구하게 된다.
    while q: ## 큐가 존재할 때까지 반복함.
        dist, now = heapq.heappop(q) ## 거리값과 현재 꺼낸 노드의 값
        if dis[now]<dist:  ## dis[1]<0  거리 값을 비교해서, 이미 처리되었으면 무시함.
            continue
        for i in graph[now]:  ## 현재 노드와 연결된 다른 인접한 노드들 확인하는 과정
            cost = dist + i[1] ## 현재 확인한 노드의 값 = dist // i[1]인접한 다른 거리 값
            if cost<dis[i[0]]: ## 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                dis[i[0]] =cost  ## cost값을 입력하고 갱신,  cost= 현재 노드를 거쳐서, 다른 노드로 이동한 거리 
                heapq.heappush(q,(cost,i[0]))

max_value=0
for i in range(1,n+1):
    count=0
    dis=[INF]*(n+1)
    dijkstra(i)
    test=dis[1:]
    for j in range(n):
        if test[j]<=m:
            count+=items[j]
            if max_value<count:
                max_value=count
print(max_value)