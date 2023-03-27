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
'''
import sys
from collections import deque
sys.stdin = open('solution/jlee14233/07. divide and conquer/입력.txt', 'r')

n,c,r =map(int,sys.stdin.readline().strip().split())

# print(n,c,r)

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


고려해야할 사항 = 2**15가 되어도 결국 위치값은 모두 동일하다는 것.
r,c =1,1 일 때, n값이 변해도 값은 3을 출력해야한다.
대충 2**r값으로 조정한 후에, c의 위치에 따라서 숫자를 변동시키는 방식은 가능한가?
4,3을 생각해보자 , 그 때 2**4 = 16이다
2의 제곱수의 위치를 일단 생각한다, 보면 첫번째 가로줄과 세로줄에만 2의 제곱수가 들어간다,
이걸 기점으로 해서 탐색을 하는 방식을 떠올리면 될거 같음. 그 때 C가 무엇을 결정하는지 생각하면 분할탐색도 필요 없이 그냥 한번에 답이 나올거 같음.

색종이 접기 혹은 쿼드모시깽으로 탐색하는 방식으로 변화시킨다면, 나머지를 0을 주고 그 rc값에만 1을 준다. 탐색을 할 때 0이면 그냥 거기까지 다 더해버린다, 그 이후 탐색부분에서 1이 나올 때까지 숫자를 그냥 더해준다. 1 탐색 직전까지의 숫자를 출력한다.

'''
'''
import sys
from collections import deque
#sys.stdin = open('solution/jlee14233/07. divide and conquer/입력.txt', 'r')

n,c,r =map(int,sys.stdin.readline().strip().split())
leng=2**n
cnt=0
mat=[[0]*leng for _ in range(leng)]
mat[c][r]=1
# print(mat)

def z_find(x,y,n):
    global cnt, r, c
    f_1=mat[x][y]
    for row in range(x,x+n):
        for col in range(y,y+n):
            if mat[x][y]==1:
                print(cnt,end='')
                quit()
            elif f_1!=mat[row][col]:
                z_find(x,y,n//2)
                z_find(x,y+n//2,n//2)
                z_find(x+n//2,y,n//2)
                z_find(x+n//2,y+n//2,n//2)
                return 0
    # print(x,y,n)    
    cnt+=n**2

    return mat
z_find(0,0,leng)

여기에서 mat을 사용하지 않고 바로 풀이를 할 수 있는 방법

'''

# def z_find(x,y,n):
#     global cnt, r, c

#     for row in range(x,x+n):
#         for col in range(y,y+n):
#             if row==r and col==c:
#                 print(cnt,end='')
#                 quit()
#             if r>n//2 and c>n//2:
#                 # print(x,y,n)
#                 z_find(x,y,n//2)
#                 z_find(x,y+n//2,n//2)
#                 z_find(x+n//2,y,n//2)
#                 z_find(x+n//2,y+n//2,n//2)
#                 return 0
#     print(x,y,n)    
#     cnt+=n**2

#     return cnt

import sys
from collections import deque
sys.stdin = open('solution/jlee14233/07. divide and conquer/입력.txt', 'r')

# n,r,c =map(int,sys.stdin.readline().strip().split())

# leng=2**n
# x,y,cnt=0,0,0

# leng=leng//2

# while x!=r and y!=c and leng!=0:
#     if r>=leng and c>=leng:
#         cnt+=3*(leng**2)
#         y+=leng
#         x+=leng
#     elif r>=leng and c<leng:
#         cnt+=2*(leng**2)
#         y+=leng        
#     elif r<leng and c>=leng:
#         cnt+=leng**2
#         x+=leng

#     leng=leng//2
#     print(x,y,leng)

# print(cnt)

N, r, c = map(int, input().split())

ans = 0

while N != 0:
	N -= 1
	if r < 2 ** N and c < 2 ** N:
		ans += ( 2 ** N ) * ( 2 ** N ) * 0
	elif r < 2 ** N and c >= 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 1
		c -= ( 2 ** N )
	elif r >= 2 ** N and c < 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 2
		r -= ( 2 ** N )
	else:
		ans += ( 2 ** N ) * ( 2 ** N ) * 3
		r -= ( 2 ** N )
		c -= ( 2 ** N )
    

print(ans)