## 소수 

'''
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.
'''
import sys

sys.stdin = open('C:/Users/tcsss/Desktop/STUDY_CODE/solution/jlee14233/01.math/입력.txt','r')

m=int(sys.stdin.readline())
n=int(sys.stdin.readline())
index= set(range(m,n+1))
a = {i for i in range(m,n+1) for j in range(2, int(i**1/2)+1) if i%j==0}
a.add(1)
## a는 소수가 아닌 수를 모두 모았다.
# print(index)
# print(a)

sol= {i for i in index if i not in a}
print(sol)
print(len(sol))
# ## 61 67 71 73 79 83 89 97
if len(sol)==0:
    print(-1)
else:
    print(sum(sol))
    print(min(sol))

# print(-1 if len(sol)==0 else sum(sol),min(sol),sep='\n')


# b= [for i in rnage(m,n+1) if i == 1 continue for j in range(2,i) if i%j == 0 break]
# b= [break if i%j==0 else ]


'''
m = int(input())
n = int(input())
prime_l = list()

def getPrime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            n = -1
            break
    if n != -1 and n != 1:
        prime_l.append(n)


for i in range(m, n+1):
    getPrime(i)

if len(prime_l) != 0:
    print(sum(prime_l))
    print(min(prime_l))
else:
    print(-1)

'''