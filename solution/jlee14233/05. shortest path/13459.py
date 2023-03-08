## 숨바꼭질 3
'''
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

'''


import sys
from collections import deque

sys.stdin = open('solution/jlee14233/05. shortest path/입력.txt', 'r')

n,k = map(int,sys.stdin.readline().strip().split())
deq=deque([n])
INF= int(1e9)
dis=[INF]*(100001)
dis[n]=0
visited=[False]*(100001)
visited[n]=True
while deq:
    nex=deq.popleft()
    if 0<=2*nex<100001 and not visited[2*nex]:
        dis[2*nex]=dis[nex]
        deq.appendleft(2*nex)
        visited[2*nex]=True
    if 0<=nex+1<100001 and not visited[nex+1]:
        dis[nex+1]=dis[nex]+1
        deq.append(nex+1)
        visited[nex+1]=True
    if 0<=nex-1<100001 and not visited[nex-1]:
        dis[nex-1]=dis[nex]+1
        deq.append(nex-1)
        visited[nex-1]=True
print(dis[k])