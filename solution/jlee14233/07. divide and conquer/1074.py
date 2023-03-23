###z
'''
문제
한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.



N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.

다음 예는 22 × 22 크기의 배열을 방문한 순서이다.



N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

다음은 N=3일 때의 예이다.



입력
첫째 줄에 정수 N, r, c가 주어진다.

출력
r행 c열을 몇 번째로 방문했는지 출력한다.

제한
1 ≤ N ≤ 15
0 ≤ r, c < 2N
'''

import sys
from collections import deque
sys.stdin = open('solution/jlee14233/07. divide and conquer/입력.txt', 'r')

n,c,r =map(int,sys.stdin.readline().strip().split())

# print(n,c,r)
'''
전수조사하는 방식이므로 이 방식을 바꿔야한다,
즉, 어느 특정 부분이 정해져있기 때문에, 그 부분을 파고 들어서 생각하는것이 좋다.
c,r의 위치에 따라서 특정 위치는 x로 가정한 후 그 다음 숫자들을 탐색하는 방식?
또한 예제의 범위가 10억단위이기 때문에 한번에 나타날 수 있도록 만들어야한다.

mat=[[[] for _ in range(2**n)] for _ in range(2**n)]
# visited=[[False for _ in range(2**n)] for _ in range(2**n)]
# print(mat)

cnt=0
leng=2**n
def z_find(x,y,n):
    global cnt,r,c
    for row in range(x,x+n):
        for col in range(y,y+n):  
            if x==r and y==c:
                print(cnt//4,end='')
                quit()    
            mat[x][y]=cnt//4
            z_find(x,y,n//2)
            z_find(x,y+n//2,n//2)
            z_find(x+n//2,y,n//2)
            z_find(x+n//2,y+n//2,n//2)
            return 0
    cnt+=1
    return mat

z_find(0,0,leng)
'''