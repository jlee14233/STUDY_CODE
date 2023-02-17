##가장 긴 증가하는 부분 수열
'''
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

'''
import math
import sys

sys.stdin = open('solution/jlee14233/03. DP/입력.txt', 'r')

n=int(sys.stdin.readline().strip())
su=list(map(int,sys.stdin.readline().strip().split()))
cnt=0
temp=su[0]
for i in su:
    print(i)
    if temp<i:
        print(i,temp)
        cnt+=1
    else:
        continue
    temp=i
print(cnt)