## 1,2,3 더하기

'''
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

'''

# import sys

# sys.stdin = open('solution/jlee14233/03. DP/입력.txt', 'r')

# n=int(sys.stdin.readline().strip())
# def sum_123(n):
#     dp=[0]*(n+3)
#     dp[1],dp[2],dp[3]=1,2,4
#     if n>=4:
#         for n in range(4,n+1):
#             dp[n]=dp[n-1]+dp[n-2]+dp[n-3]
#     return dp[n]

# for i in range(n):
#     i=int(sys.stdin.readline().strip())
#     print(sum_123(i)) 

# ## 1,2,3 더하기 4

'''
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
1+1+1+1
2+1+1 (1+1+2, 1+2+1)
2+2
1+3 (3+1)
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
dp[1] = 1
dp[2] = 2
dp[3] = 1+1+1, 2+1, 3, 3
dp[4] =1+1+1 , 2+1+1, 3+1, 2+2      :4 
dp[5] =1+1+1+1+1 , 2+1+1+1,3+1+1, 2+2+1, 3+2, 5?
dp[6]=7
dp[7]=8
dp[8]=10
dp[9]=11
dp[10]=14


a_n​=a_{n−3}​+⌊n/2​⌋+1(n: 자연수,a₁=1,a₂=2,a₃​=3)

'''

import sys

sys.stdin = open('solution/jlee14233/03. DP/입력.txt', 'r')

# n=int(sys.stdin.readline().strip())
# def sum_123(n):
#     dp=[1]*(n+3)
#     if n>=4:
#         for n in range(4,n+1):
#             dp[n]=dp[n-3]+2
#     return dp[n]

# for i in range(n):
#     i=int(sys.stdin.readline().strip())
#     print(sum_123(i)) 

# import sys

T = int(sys.stdin.readline())
dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]
print(dp)
    
for i in range(3, 10001):
    dp[i] += dp[i - 3]
print(dp)
for i in range(T):
    n = int(sys.stdin.readline())
    print(dp[n])

'''
점화식을 찾지 못해서 못 푼 문제.
'''