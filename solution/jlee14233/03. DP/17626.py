## four squares
'''
문제
라그랑주는 1770년에 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다고 증명하였다. 어떤 자연수는 복수의 방법으로 표현된다. 예를 들면, 26은 52과 12의 합이다; 또한 42 + 32 + 12으로 표현할 수도 있다. 역사적으로 암산의 명수들에게 공통적으로 주어지는 문제가 바로 자연수를 넷 혹은 그 이하의 제곱수 합으로 나타내라는 것이었다. 1900년대 초반에 한 암산가가 15663 = 1252 + 62 + 12 + 12라는 해를 구하는데 8초가 걸렸다는 보고가 있다. 좀 더 어려운 문제에 대해서는 56초가 걸렸다: 11339 = 1052 + 152 + 82 + 52.

자연수 n이 주어질 때, n을 최소 개수의 제곱수 합으로 표현하는 컴퓨터 프로그램을 작성하시오.

입력
입력은 표준입력을 사용한다. 입력은 자연수 n을 포함하는 한 줄로 구성된다. 여기서, 1 ≤ n ≤ 50,000이다.

출력
출력은 표준출력을 사용한다. 합이 n과 같게 되는 제곱수들의 최소 개수를 한 줄에 출력한다.


'''

import sys
import math

sys.stdin = open('solution/jlee14233/03. DP/입력.txt', 'r')
n=int(sys.stdin.readline().strip())
def sqr(n):
    sqr=[i*i for i in range(1,224)]
    dp=[0 for _ in range(n+1)]
    for i in range(1,n+1):
        if i in sqr:
            dp[i]=1
        else:
            for j in sqr:
                if i-j>0:
                    dp[i]=min(dp[i-j])+1
                
            dp[i]=min([dp[i-j] for j in sqr if i-j>0])+1
    return(dp[i])

print(sqr(n))        


n = int(input())

s = {i**2 for i in range(1, int(n ** 0.5) + 1)}


def a(n):
    if (n ** 0.5).is_integer():
        return 1


    for t in s:
        if n - t in s:
            return 2

    for i in s:
        for j in s:
            if n - i - j in s:
                return 3

    return 4


print(a(n))

'''
점화식을 다시 수정하였다.
만약 sqr 숫자일 경우에는 1을 출력하도록 한다
특정 숫자 + 제곱수 숫자 = 제곱수 숫자 조합이다
따라서 D(n+1) = D(n) +1
인데, 이 때 가장 작은 수를 선별해서 넣기 위해서 list comprehension으로 처리 한 후 min 값을 넣고 , +1 을 넣는다.
밑의 방식은 브루트 포스 방식으로 찾아 본 것.


'''