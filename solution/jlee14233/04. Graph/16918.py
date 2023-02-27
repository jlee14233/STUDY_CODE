## 봄버맨
'''
문제
봄버맨은 크기가 R×C인 직사각형 격자판 위에서 살고 있다. 격자의 각 칸은 비어있거나 폭탄이 들어있다.

폭탄이 있는 칸은 3초가 지난 후에 폭발하고, 폭탄이 폭발한 이후에는 폭탄이 있던 칸이 파괴되어 빈 칸이 되며, 인접한 네 칸도 함께 파괴된다. 즉, 폭탄이 있던 칸이 (i, j)인 경우에 (i+1, j), (i-1, j), (i, j+1), (i, j-1)도 함께 파괴된다. 만약, 폭탄이 폭발했을 때, 인접한 칸에 폭탄이 있는 경우에는 인접한 폭탄은 폭발 없이 파괴된다. 따라서, 연쇄 반응은 없다.

봄버맨은 폭탄에 면역력을 가지고 있어서, 격자판의 모든 칸을 자유롭게 이동할 수 있다. 봄버맨은 다음과 같이 행동한다.

가장 처음에 봄버맨은 일부 칸에 폭탄을 설치해 놓는다. 모든 폭탄이 설치된 시간은 같다.
다음 1초 동안 봄버맨은 아무것도 하지 않는다.
다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다. 즉, 모든 칸은 폭탄을 가지고 있게 된다. 폭탄은 모두 동시에 설치했다고 가정한다.
1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다.
3과 4를 반복한다.
폭탄을 설치해놓은 초기 상태가 주어졌을 때, N초가 흐른 후의 격자판 상태를 구하려고 한다.

풀이 생각
1초 -> 전체를 0으로 만든다
2초 -> 터진 부위 상하좌우만 . 으로 변경한다
3초 -> 전체를 0으로 만든다.
4초 -> 초기값으로 돌아온다. -> 2초에서 터진걸 다시 .으로 만들어야한다.

초기값과 4초가 다른 값으로 나옴. 그래서 반례가 존재하는 듯 하다.
즉 그냥 %4에 따라서 어떻게 만들어지는지만 출력하도록 만들면 될 것 같음.

'''
import sys
from collections import deque

sys.stdin = open('solution/jlee14233/04. Graph/입력.txt', 'r')

r,c,n =map(int,sys.stdin.readline().strip().split())
ad_mat=[list(map(str,sys.stdin.readline().strip())) for i in range(r)]
twofour=[['O' for _ in range(c)] for _ in range(r)]


dx=[1,-1,0,0]
dy=[0,0,-1,1]

bomb=[(i,j) for i in range(r) for j in range(c) if ad_mat[i][j]=='O']
aft=[_[:] for _ in twofour]

while bomb:
    x,y =bomb.pop()
    aft[x][y]='.'
    for i in range(4):
        xx= x+dx[i]
        yy= y+dy[i]

        if 0<=xx<r and 0<=yy<c:
            aft[xx][yy]='.'
bomb_2=[(i,j) for i in range(r) for j in range(c) if aft[i][j]=='O']
aft_2=[_[:] for _ in twofour]
while bomb_2:
    x,y =bomb_2.pop()
    aft_2[x][y]='.'
    for i in range(4):
        xx= x+dx[i]
        yy= y+dy[i]

        if 0<=xx<r and 0<=yy<c:
            aft_2[xx][yy]='.'

if n==1:
    for _ in ad_mat:print(*_,sep='')
elif n%4==2 or n%4==0:
    for _ in twofour:print(*_,sep='')
elif n%4==3:
    for _ in aft:print(*_,sep='')
elif n%4==1 and n>=5:
    for _ in aft_2:print(*_,sep='')
        