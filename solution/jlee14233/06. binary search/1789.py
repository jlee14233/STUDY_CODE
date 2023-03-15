## 수들의 합
'''
문제
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

입력
첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

출력
첫째 줄에 자연수 N의 최댓값을 출력한다.

200 -> 100-> 50-> 25-> 12->6->3->2->1?
이게 왜 이분탐색일까?

n이 최대가 되기 위해서는 1부터 시작을 해야함.
start값이 1이고 end값이 s일 경우를 가정해서 풀이를 한다.

'''


import sys
import time
sys.stdin = open('solution/jlee14233/06. binary search/입력.txt', 'r')

s= int(sys.stdin.readline().strip())

# start=1
# end=s
# t=((start+end)*(end-(start-1)))/2
# t_1=((start+end+1)*(end-(start)+2))/2
# mid =(start+end+1)//2
# if s==1 or s==2:
#     print(1)
#     quit()
# else:
#     while True:
#         if t>s:
#             end=mid
#         else:
#             end=end+1
#         mid =(start+end+1)//2
#         t=((start+end)*(end-(start-1)))/2
#         t_1=((start+end+1)*(end-(start)+2))/2
#         if t<=s and s<=t_1:
#             if t_1==s:
#                 end+=1
#             print(start,end,t,t_1,mid)
#             break
            
# print(end)

'''
위에서 푼 방식은 반절만 이진 탐색을 실행하고 나머지는 순차탐색을 진행해버림.
아직 개념에 대해서 익숙해지지 못했기 때문에 이렇게 문제가 발생해버렸다.
만약 시간 제한이 엄청 타이트 했다면 위의 방식은 풀이에 문제가 발생했을 것.

'''
def max_n(s):
    left ,right =1,s
    while left<=right:
        mid=(left+right)//2
        temp=mid*(mid+1)//2
        if temp <=s:
            left = mid+1
        else:
            right = mid-1
        print(left,right)
    return right

print(max_n(s))