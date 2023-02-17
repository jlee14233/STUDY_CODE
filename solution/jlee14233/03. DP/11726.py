##2×n 타일링

'''
문제
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.


'''

import sys

sys.stdin = open('solution/jlee14233/03. DP/입력.txt', 'r')
n=int(sys.stdin.readline().strip())

a=1
b=1
for i in range(0,n):
    a,b=a+b,a

print(b%10007)

'''
구해보니까 n=(n-1)+(n-2)이라는 점화식이 발생해서
피보나치와 동일했다
그래서 그냥 반복문 처리로 가장 빠르게 푸는 방식으로 변경함.

'''