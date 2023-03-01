## 토마토 2

'''

문제
철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자모양 상자의 칸에 하나씩 넣은 다음, 상자들을 수직으로 쌓아 올려서 창고에 보관한다.



창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다. 둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다. 각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 이러한 N개의 줄이 H번 반복하여 주어진다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

출력
여러분은 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

'''



import sys
from collections import deque
import time
from functools import reduce
import itertools
import operator

sys.stdin = open('solution/jlee14233/04. Graph/입력.txt', 'r')

n,m,l =map(int,sys.stdin.readline().strip().split())

box=[]
to_1=deque([])

'''
시간을 뺐기는 요소가 오히려 이곳에 있는 듯 해서 밑을 단순하게 바꾸는 게 더 좋음. 
list comprehension으로 배열을 만들고,
그냥 1이 있는 것만 찾아서 따로 저장하는 시스템이 더 빠른 듯 하다.
https://codechacha.com/ko/python-flatten-list/#5-list-comprehension%EC%9C%BC%EB%A1%9C-2%EC%B0%A8%EC%9B%90---1%EC%B0%A8%EC%9B%90-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EB%B3%80%ED%99%98
여기에서 차원 낮추는 방법을 봄.

'''
for c in range(l): ## z
    floor=[]
    for b in range(m): ## y
        num=list(map(int,sys.stdin.readline().strip().split()))
        for a in range(n): ## x
            if num[a]==1:
                to_1.append([a,b,c,0])
        floor.append(num)
    box.append(floor)
dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]
cnt=0

while to_1:
    node=to_1.popleft()
    for i in range(6):
        zz= node[2]+dz[i]
        yy= node[1]+dy[i]
        xx= node[0]+dx[i]
        if 0<=xx<n and 0<=yy<m and 0<=zz<l and box[zz][yy][xx]==0:
            box[zz][yy][xx]=node[3]+1
            to_1.append([xx,yy,zz,node[3]+1])
        if cnt<(node[3]):
            cnt=node[3]


## 여기에서는 3차원 탐색하면서 0만 발견하면 -1을 출력하고 바로 quit하는 형식의 알고리즘으로 구현하였다.
start=time.time()
for i in box:
    for j in i:
        for k in j:
            if  k==0:
                print(-1)
                quit()
print(cnt)
end=time.time()
print('3중 for문 ',f"{end - start:.5f} sec")

## 시간 복잡도가 O(N^2) 시간 초과가 발생하게 된다. sum을 이용했을 경우./ 결국 n^2를 모두 돈 다음에 정리를 해서 존재유무를 파악하기 때문에 중도 중단이 아니라서 시간초과가 나는 느낌이다. 위의 식과 사실상 다를게 없음.

start=time.time()
box =sum(box,[])
box =sum(box,[])
box=set(box)
print(box) ##리스트 차원을 낮추고 set과 list로 재변환해서 0이 존재하는지 아닌지만 따지면 된다?
if 0 in box:
    print(-1)
else:
    print(cnt)
end=time.time()

print('sum=:'f"{end - start:.5f} sec")

## 만약 reduce나 list comprehension을 이용하게 되면 어떨까?

start=time.time()
box = set(list(itertools.chain.from_iterable(list(itertools.chain.from_iterable(box)))))
print(box)
if 0 in box:
    print(-1)
else:
    print(cnt)
end=time.time()
print('itertools=',f"{end - start:.5f} sec")

# start=time.time()
box = set(list(reduce(operator.add,list(reduce(operator.add,box)))))
print(box)
if 0 in box:
    print(-1)
else:
    print(cnt)
end=time.time()
print('reduce=',f"{end - start:.5f} sec")
## sum과 같은 형식이기 때문에 시간이 걸리는 것을 확인.

start=time.time()
box=set([data for inner in box for outer in inner for data in outer])
print(box)
if 0 in box:
    print(-1)
else:
    print(cnt)
end=time.time()
print('list comprehension=',f"{end - start:.5f} sec")
