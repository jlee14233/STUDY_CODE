##가장 긴 증가하는 부분 수열
'''
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.


memo=[[0 for _ in range(m+1)] for _ in range(n+1)]
'''
import math
import sys

sys.stdin = open('solution/jlee14233/03. DP/입력.txt', 'r')

n=int(sys.stdin.readline().strip())
su=list(map(int,sys.stdin.readline().strip().split()))

l=[1]*n

for i in range(1,n):
    for j in range(i):
        if su[i]>su[j]:
            l[i]=max(l[i],l[j]+1)
    print(l)
print(max(l))
