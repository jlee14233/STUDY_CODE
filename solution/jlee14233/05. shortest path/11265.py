## 끝나지 않는 파티
'''
파티를 좋아하는 민호는 끝없이 파티가 열리는 놀이동산 "민호월드"를 세웠다. 처음에는 한개의 파티장만을 가지고 있는 작은 놀이동산이었지만, 사람들의 점점 많이 찾아와 파티장을 증축했고 현재는 N개의 파티장을 가진 큰 놀이동산이 되었다. 민호는 파티장을 증축할때마다 편의를 위해 새로운 파티장과 기존의 모든 파티장이 직접적으로 연결이 될 수 있는 도로들을 만들었다. 이때 만들어진 도로들은 사용자들의 편의를 위해 일방통행으로 설계가 되었다.

파티장이 적을때는 괜찮았지만 파티장이 많아진 지금 다음과 같은 두 가지 문제점이 발생했다.

A 파티장에서 B 파티장으로 빨리 갈 수 있도록 직접 연결이 된 일방통행 도로를 만들었지만 A와 B가 아닌 다른 파티장을 경유해서 더 빨리 갈 수 있는 경우가 있을 수 있다.
지금으로부터 C만큼의 시간 뒤에 B번 파티장에서 새롭게 파티가 열리는데 1번과 같은 이유때문에 현재 있는 A파티장에서 B번 파티장까지 파티가 열리는 시간까지 맞춰 갈 수 있는지 쉽게 알 수 없다.

이러한 문제점으로 이용객들의 불만이 점점 커져갔고 민호는 이를 해결하기 위해 빠른 네비게이션 서비스를 실행하기로 하였으나 서비스 요청이 너무 많아 업무가 마비되기에 이르렀다. 이에 민호는 천재프로그래머인 당신에게 이 문제를 해결해 달라고 요청하였다. 민호를 도와 한 파티장에서 다른 파티장에까지 시간내에 도착할 수 있는지 없는지 알아봐주는 프로그램을 작성하자.

입력
입력의 첫 번째 줄에는 파티장의 크기 N(5 ≤ N ≤ 500)과 서비스를 요청한 손님의 수 M(1 ≤ M ≤ 10,000) 이 주어진다. 각각의 파티장은 1번부터 N번까지 번호가 붙여져 있다. 다음에는 N개의 줄에 걸쳐 각각 N개의 수가 주어진다. i번째 줄의 j번째 수 T(1 ≤ T ≤ 1,000,000)는 i번 파티장에서 j번 파티장으로 직접적으로 연결된 도로를 통해 이동하는 시간을 의미한다.

다음 M개의 줄에는 세개의 정수 A, B, C가 주어진다. A(1 ≤ A ≤ N) 는 서비스를 요청한 손님이 위치한 파티장의 번호, B(1 ≤ B ≤ N) 다음 파티가 열리는 파티장의 번호, C(1 ≤ C ≤ 1,000,000,000)는 지금으로부터 다음 파티가 열리는데 걸리는 시간을 의미한다.

출력
M개의 줄에 걸쳐 서비스를 요청한 손님이 시간내에 다른 파티장에 도착할 수 있으면 “Enjoy other party”를, 시간내에 도착할 수 없으면 "Stay here”를 출력한다.
'''
import sys
from collections import deque
from collections import defaultdict

sys.stdin = open('solution/jlee14233/05. shortest path/입력.txt', 'r')

INF =int(1e9)

n,m=map(int,sys.stdin.readline().strip().split())

graph=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])


for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().strip().split())
    if graph[a-1][b-1]<=c:
        print('Enjoy other party')
    else:
        print('Stay here')

## python3로 돌릴 경우 시간 초과 pypy3로 돌릴 경우 ok 
