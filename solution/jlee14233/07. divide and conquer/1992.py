## 쿼드트리
'''
문제
흑백 영상을 압축하여 표현하는 데이터 구조로 쿼드 트리(Quad Tree)라는 방법이 있다. 흰 점을 나타내는 0과 검은 점을 나타내는 1로만 이루어진 영상(2차원 배열)에서 같은 숫자의 점들이 한 곳에 많이 몰려있으면, 쿼드 트리에서는 이를 압축하여 간단히 표현할 수 있다.

주어진 영상이 모두 0으로만 되어 있으면 압축 결과는 "0"이 되고, 모두 1로만 되어 있으면 압축 결과는 "1"이 된다. 만약 0과 1이 섞여 있으면 전체를 한 번에 나타내지를 못하고, 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래, 이렇게 4개의 영상으로 나누어 압축하게 되며, 이 4개의 영역을 압축한 결과를 차례대로 괄호 안에 묶어서 표현한다



위 그림에서 왼쪽의 영상은 오른쪽의 배열과 같이 숫자로 주어지며, 이 영상을 쿼드 트리 구조를 이용하여 압축하면 "(0(0011)(0(0111)01)1)"로 표현된다. N ×N 크기의 영상이 주어질 때, 이 영상을 압축한 결과를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 영상의 크기를 나타내는 숫자 N 이 주어진다. N 은 언제나 2의 제곱수로 주어지며, 1 ≤ N ≤ 64의 범위를 가진다. 두 번째 줄부터는 길이 N의 문자열이 N개 들어온다. 각 문자열은 0 또는 1의 숫자로 이루어져 있으며, 영상의 각 점들을 나타낸다.

출력
영상을 압축한 결과를 출력한다.

색종이 만들기와 유사한 문제같음
'''


import sys
from collections import deque
import time
sys.stdin = open('solution/jlee14233/07. divide and conquer/입력.txt', 'r')

n= int(sys.stdin.readline().strip())
mat=[list(map(int,*sys.stdin.readline().strip().split())) for _ in range(n)]

'''
조건을 따져야함.
1 1234분면으로 나눈다
2 나눠진 분면이 모두 동일한 숫자인지 확인한다.
3. 모두 동일한 숫자일 경우 그 숫자로 표기한다.
4. 아닐 경우 다시 분면을 1234 분면으로 나눈다.
5. 위를 반복한다. (재귀)

'''
def quad_tree(x,y,n):
    
    color = mat[x][y]
    for row in range(x,x+n):
        for col in range(y,y+n):
            if color!=mat[row][col]:
                print('(',end='')
                quad_tree(x,y,n//2)
                quad_tree(x,y+n//2,n//2)
                quad_tree(x+n//2,y,n//2)
                quad_tree(x+n//2,y+n//2,n//2)
                print(')',end='')
                return 

    print(mat[x][y],end='')
    return

quad_tree(0,0,n)
# a=output.popleft()
# result.append([a[0]])
# while output:
#     b=output.popleft()
#     if b[1]==a[1]:
#         result[-1].append(b[0])
#     else:
#         result.append([b[0]])
#     a=b
# print(result)

## 위를 4개씩 끊어서 생각해야할듯. 이거 다녀와서 다시 풀이할 것.
# []