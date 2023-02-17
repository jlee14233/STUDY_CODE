##조합

'''
nCm출력하기

'''
import math
import sys

sys.stdin = open('solution/jlee14233/03. DP/입력.txt', 'r')

n=list(map(int,sys.stdin.readline().strip().split()))
print(n)
print(math.comb(n[0],n[1]))

def combi(n,m):
    tab=[i for i in range(1,101)]
    result = math.prod(tab[n-m:n])//math.prod(tab[1:m])
    return result

print(combi(100,6))