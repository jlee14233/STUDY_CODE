##다리 놓기
'''
재원이는 한 도시의 시장이 되었다. 이 도시에는 도시를 동쪽과 서쪽으로 나누는 큰 일직선 모양의 강이 흐르고 있다. 하지만 재원이는 다리가 없어서 시민들이 강을 건너는데 큰 불편을 겪고 있음을 알고 다리를 짓기로 결심하였다. 강 주변에서 다리를 짓기에 적합한 곳을 사이트라고 한다. 재원이는 강 주변을 면밀히 조사해 본 결과 강의 서쪽에는 N개의 사이트가 있고 동쪽에는 M개의 사이트가 있다는 것을 알았다. (N ≤ M)

재원이는 서쪽의 사이트와 동쪽의 사이트를 다리로 연결하려고 한다. (이때 한 사이트에는 최대 한 개의 다리만 연결될 수 있다.) 재원이는 다리를 최대한 많이 지으려고 하기 때문에 서쪽의 사이트 개수만큼 (N개) 다리를 지으려고 한다. 다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라.


'''
import sys
import time

sys.stdin = open('solution/jlee14233/03. DP/입력.txt', 'r')
n=int(sys.stdin.readline().strip())
'''
점화식은 완성했음
F(i+1)(j+1)=F(i+1)(j)+F(i)(j)
'''

# 이렇게 풀기에는 너무 많은 것을 계산하는느낌. 너무 느리다!
def brg(i,j):
    memo=[[0 for j in range(j+1)]for i in range(i+1)]
    if i==j:
        return 1
    if i==1:
        memo[i][j]=j
    if memo[i][j]!=0:
        return memo[i][j]
    else:
        memo[i][j]=brg(i-1,j-1)+brg(i,j-1)
        return memo[i][j]
## 위의 방식은 메모이제이션 방식.
## 밑의 방식은 타뷸레이션 방식.


def brg_T(n,m):
    memo=[[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 :
                memo[i][j]=j
                continue
            if i == j:
                memo[i][j]=1
            else:
                if j>i:
                    memo[i][j]=memo[i][j-1]+memo[i-1][j-1]
    return memo[i][j]


# start=time.time()
# print(brg(13,24))
# end=time.time()

# start1=time.time()
# print(brg_T(13,24))
# end1=time.time()

# print(f"{end - start:.5f} sec")
# print(f"{end1 - start1:.5f} sec")


for i in range(n):
    i,j = map(int,sys.stdin.readline().strip().split())
    print(brg_T(i,j))