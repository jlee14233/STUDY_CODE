## 서로소 평균
'''
첫 번째 줄에 입력될 수들의 개수 
$N$이 주어진다. 
$(2 \le N \le 500,000)$ 

두 번째 줄에는 수열 
$A$를 이루는 자연수 
$A_{i}$ 가 공백으로 구분되어 주어진다. 
$(2 \le A_{i} \le 1,000,000)$ 

수열 
$A$에 
$X$와 서로소인 수가 최소 1개 이상 존재한다.

마지막 줄에는 
$X$가 주어진다. 
$(2\le X \le 1,000,000)$ 
'''

def gcd(a,b):
    while b!=0:
        r = a%b
        a = b
        b = r
    return a


import sys
import math

sys.stdin = open('C:/Users/tcsss/Desktop/STUDY_CODE/solution/jlee14233/입력.txt','r')

n=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
x=int(sys.stdin.readline())

sol =[A[a] for a in range(0,n) if math.gcd(x,A[a])==1]

print(sum(sol)/len(sol))


# remove_set={0}
# sol= [i for i in sol if i not in remove_set] 0을 포함 했을 때의 풀이 0을 처음부터 안넣는 방식으로 바꾸었다.

# sol = set([A[a] if math.gcd(x,A[a])==1 else 0 for a in range(0,n)])
# sol.remove(0)
# print (sum(sol)/(len(sol)-1))  처음의 잘못된 풀이

'''
N = int(input())
A = list(map(int, input().split()))
X = int(input())

bunja = 0
bunmo = 0

for a in A:
    if math.gcd(X, a) == 1: bunja += a; bunmo += 1

백준의 다른 사람의 풀이, 분자 분모를 카운팅하는 방식으로 해결하였다. (시간은 이쪽이 더 빠르게 나타남.)
'''
