## 더하기 사이클

'''
str로 받은 문자열을 int를 활용하여 계속 더하는 사이클을 만든다.
이때 str의 문자열이 1개일 경우와 2개일 경우를 나눠서 계산한다.
10 미만-> 0n로 처리
10 미만의 처리 len(n)이 1일 경우

'''

import sys

sys.stdin = open('C:/Users/tcsss/Desktop/STUDY_CODE/solution/jlee14233/입력.txt','r')

N=input()
count=0
n=N
while True:
    if len(n)==1:
        a=0
        b=n[-1]
        c=int(a)+int(b)
        n=str(b)+str(c)[-1]
        count+=1
    else:
        a=n[0]
        b=n[-1]
        
        c=int(a)+int(b)
        n=str(b)+str(c)[-1]

        count+=1
    
    if int(n)==int(N):
        break

print(count)

x = int(input())
num = x
count = 0

while 1:
    a = num//10
    b = num%10
    c = (a+b)%10
    num = (b*10) + c
    count += 1
    if (num == x):
        break
print(count)