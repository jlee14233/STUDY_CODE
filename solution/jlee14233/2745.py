## 진법 변환

'''
B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.

10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35


'''


import sys

sys.stdin = open('C:/Users/tcsss/Desktop/STUDY_CODE/solution/jlee14233/입력.txt','r')

a,b=map(str,input().split())

# '''간단한 풀이방법'''
# print(int(data[0],int(data[1])))

index='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# print(index.find('Z'))

i = [index.find(a[sol])*(int(b)**(len(a)-1-sol)) for sol in range(0,len(a))]

print(sum(i))
