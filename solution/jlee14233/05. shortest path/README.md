# Shortest path.
---
최단 경로 알고리즘에는 크게 두 가지 방식이 있다.
- 다익스트라 알고리즘
- 플로이드 워셜 알고리즘

## 다익스트라 알고리즘

그래프에서 여러 개의 노드가 있을 경우, 특정 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘이다.
이 때, 음의 간선이 없을 경우에 정상적으로 작동하는 것에 유의한다.

#### 동작 방식

1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
5. 위의 3~4번 과정 반복

다익스트라 알고리즘은 최단 경로를 구하는 과정에서 최대 거리 정보를 1차원 리스트에 저장한 후, 리스트를 계속 갱신한다는 특징이 있다.

#### 구현
알고리즘 그대로 구현한 다익스트라 알고리즘의 경우 시간복잡도가 O(V^2)를 갖게 된다. 이 때 V는 노드의 개수이다.
밑은 간단한 구현 방식이다.
```python
## 간단한 방식의 파이썬 구현 식
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
```
<a href='https://freedeveloper.tistory.com/384'>

##### 간단한 방식의 다익스트라 구현 성능 분석

- O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 한다.
- 따라서 시간 복잡도는 O(V^2)이다.
- 이 경우 전체 노드의 개수가 5000개 이하라면 이 코드로 문제가 해결되지만 노드의 수가 증가하면 시간 초과가 발생할 가능성이 높다.

#### 구현 2 - 우선 순위 큐 활용





