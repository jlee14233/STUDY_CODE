## 선분 위의 점

'''
문제
일차원 좌표상의 점 N개와 선분 M개가 주어진다. 이때, 각각의 선분 위에 입력으로 주어진 점이 몇 개 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N과 선분의 개수 M이 주어진다. (1 ≤ N, M ≤ 100,000) 둘째 줄에는 점의 좌표가 주어진다. 두 점이 같은 좌표를 가지는 경우는 없다. 셋째 줄부터 M개의 줄에는 선분의 시작점과 끝점이 주어진다. 입력으로 주어지는 모든 좌표는 1,000,000,000보다 작거나 같은 자연수이다.

출력
입력으로 주어진 각각의 선분 마다, 선분 위에 입력으로 주어진 점이 몇 개 있는지 출력한다.

해당 범위 안에 있는지 확인하기만 하면 되는 문제.
'''

import sys
from collections import defaultdict
sys.stdin = open('solution/jlee14233/06. binary search/입력.txt', 'r')

n,m= map(int,sys.stdin.readline().strip().split())

point=sorted(list(map(int,sys.stdin.readline().strip().split())))

def binary_search(array, target):
    start=0
    end=n-1
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return start,mid,end

for _ in range(m):
    a,b= map(int,sys.stdin.readline().strip().split())
    left=binary_search(point,a)
    right=binary_search(point,b)
    print(left,right)
    if isinstance(left,tuple):
        left=left[0]
    if isinstance(right,tuple):
        right=right[-1]
    print(right-left+1)
    

