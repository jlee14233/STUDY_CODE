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
[참조 문서](https://freedeveloper.tistory.com/384')

##### 간단한 방식의 다익스트라 구현 성능 분석

- O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 한다.
- 따라서 시간 복잡도는 O(V^2)이다.
- 이 경우 전체 노드의 개수가 5000개 이하라면 이 코드로 문제가 해결되지만 노드의 수가 증가하면 시간 초과가 발생할 가능성이 높다.

#### 구현 2 - 우선 순위 큐 활용
##### 우선순위 큐란?

    우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조이다.

    사용 예시: 여러 개의 물건 데이터를 자료구조에 넣었다가 높은 물건 데이터부터 꺼내서 확인하는 경우에 사용하게 된다.

##### Heap (힙)

- 우선순위 큐를 구현하기 위해 사용하는 자료구조이다.
- 최소 힙과, 최대 힙이 있다.
- 힙의 경우 삽입 시간과 삭제 시간에 드는 시간 복잡도는 O(logN)이다.
- 리스트보다 시간복잡도가 낮기 때문에, 활용이 용이하다


단계마다 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택하기 위해서 리스트 대신 힙을 사용한다.

이 때, 최단 거리가 가장 짧은 노드를 선택해야 하므로, 최소 힙을 사용한다.

```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

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

##### 개선된 방식의 다익스트라 구현 성능 분석

- 힙 자료구조를 활용하기 때문에 시간복잡도는 O(ElogV)이다
- 노드를 하나씩 꺼내 검사하는 while문은 노드의 개수 V 이상의 회수로는 처리되지 않는다. 그 결과 노드를 확인하는 총 횟수는 최대 간선의 개수만큼만 연산이 수행된다.
- 전체 과정이 E개의 원소를 우선순위 큐에 넣었다 빼는 연산과 유사하게 작동된다.

## 플로이드 워셜 알고리즘

- 다익스트라 알고리즘은 한 지점에서 다른 특정 지점까지의 최단 경로를 구할 때 사용한다면,
- 플로이드 워셜 알고리즘은 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구할 때 사용하는 알고리즘이다.
- 매 단계마다 거쳐가는 노드를 기준으로 알고리즘을 수행하며, 방문하지 않은 노드 중 최단 거리를 갖는 노드를 찾을 필요가 없다.
- 2차원 리스트를 최단 거리 테이블로 사용하게 되며, 매 단계마다 2차원 리스트를 처리하므로 시간복잡도는 O(N^3)이다.
- 다이나믹 프로그래밍 방식이므로, 플로이드 워셜의 점화식은 아래와 같다.

    D_ab= min(D_ab,D_ak+D_kb)

#### 동작 방식
1. 그래프를 준비하고 최단 거리 테이블을 초기화 한다.
2. 노드를 거쳐가는 경우를 고려하여 테이블을 갱신한다.
4. 위의 방식을 노드의 처음부터 끝까지 반복한다.

```python
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == 1e9:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()
```
[참조 문서](https://freedeveloper.tistory.com/385')

#### 플로이드 워셜 알고리즘 성능 분석
- 노드의 개수가 N일 때 알고리즘 상 N번의 단계를 수행한다.
    - 각 단계마다 테이블의 연산을 통해 노드를 거쳐가는 경로를 모두 고려한다.
- 따라서 시간복잡도가 O(N^3)가 된다.