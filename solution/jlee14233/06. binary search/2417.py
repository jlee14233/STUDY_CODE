## 정수 제곱근
'''
문제
정수가 주어지면, 그 수의 정수 제곱근을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 n이 주어진다. (0 ≤ n < 2^63)

출력
첫째 줄에 q^2 ≥ n인 가장 작은 음이 아닌 정수 q를 출력한다.

'''
import sys
import math
from decimal import Decimal
import time
sys.stdin = open('solution/jlee14233/06. binary search/입력.txt', 'r')

n=int(sys.stdin.readline().strip())

# def binary_search(target):
#     start=0
#     end=target
#     while True:
#         mid = (start + end) // 2
#         if mid*mid == target:
#             return mid
#             break
#         elif mid*mid >target:
#             end = mid-1
#         else:
#             start = mid +1
#         print(mid)
#         return mid, end, start

# print(binary_search(n))
# start=0
# end=n
# while True:

#     mid = (start+end)//2
#     if mid*mid==n:
#         print(mid)
#         break
#     elif mid*mid >n:
#         end = mid-1
#     else:
#         start = mid+1
    
#     print(mid)

def binary(target):
    start=0
    end=target
    while start<=end:
        mid = (start+end)//2
        if mid*mid >target:
            end = mid-1
        else:
            start = mid+1
    return end

e=Decimal(str(n))

if e.sqrt()==int(e.sqrt()):
    print(binary(n))
else:
    print(binary(n)+1)