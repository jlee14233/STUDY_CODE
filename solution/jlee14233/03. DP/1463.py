## 1로 만들기
'''
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
'''

import sys

sys.stdin = open('solution/jlee14233/03. DP/입력.txt', 'r')


n=int(sys.stdin.readline().strip())
## 타뷸레이션 방식
## 404ms
## 에러가 발생한 지점 dp[0]*n+1 일 때  n이 2라면 index에러가 발생하므로 테이블을 늘려줌으로써 해결함
def opr(n):
    dp=[0]*(n+3)
    dp[0],dp[1]=0,0
    if n>=2:
        dp[2],dp[3]=1,1
        for i in range(4,n+1):
            if i%2==0 and i%3==0:
                dp[i]=min(dp[i-1],dp[int(i//2)],dp[int(i//3)])+1
            elif i%2==0:
                dp[i]=min(dp[i-1],dp[int(i//2)])+1
            elif i%3==0:
                dp[i]=min(dp[i-1],dp[int(i//3)])+1
            else:
                dp[i]=dp[i-1]+1
    elif n==1:
        dp[1]=0
    return dp[n]

print(opr(n))

##메모이제이션 방식
##40ms
x=int(input())
dp={1:0, 2:1}
def rec(n):
    if n in dp.keys():
        return dp[n]
    if (n%3==0) and (n%2==0):
        dp[n]=min(rec(n//3)+1, rec(n//2)+1)
    elif n%3==0:
        dp[n]=min(rec(n//3)+1, rec(n-1)+1)
    elif n%2==0:
        dp[n]=min(rec(n//2)+1, rec(n-1)+1)
    else:
        dp[n]=rec(n-1)+1
    return dp[n]
print(rec(x))

'''
이 문제에 대해서는 확실하게 메모이제이션 하향식 방식이 훨씬 더 빠르게 문제 풀이가 가능함.
숫자 1개에 대해서 모두 고려하기 보단 덜 계산하기 때문으로 보임.
'''