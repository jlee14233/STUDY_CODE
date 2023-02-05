##다음 소수
'''
정수 n(0 ≤ n ≤ 4e9)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.
'''

import sys
import math
sys.stdin = open('C:/Users/tcsss/Desktop/STUDY_CODE/solution/jlee14233/01.math/입력.txt','r')


# index=[True]*int(data[-1])
# index[0]=False
# index[1]=False
# p=[]
# for i in range(2,len(index)+1):
#     for j in range(i+i,len(index),i):
#         if index[j]==False:
#             continue
#         index[j]=False

# print(index)
# print(p)
def prime(t):
    if t==0 or t==1 :
        return False
    for i in range(2,int(math.sqrt(t))+1):
        if t%i ==0:
            return False

    return True
n=int(sys.stdin.readline())

for i in range(n):
    z=int(sys.stdin.readline())
    while True:
        if prime(z):
            print(z)
            break
        else:
            z+=1
