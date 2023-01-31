##피로도
'''
피로도 A 일 처리 B 한 시간 쉴 경우 피로도 C 감소
피로도는 M을 넘지 않게 일을 한다. M이 넘을 경우 일을 그만둔다.
번아웃이 되지 않도록 하루에 할 수 있는 최대의 일의 량은? 
5 3 2 10

피로도 0

'''

import sys

sys.stdin = open('C:/Users/tcsss/Desktop/STUDY_CODE/solution/jlee14233/입력.txt','r')

data=list(map(int,input().split()))
stress=0
work=0
for i in range(0,24):
    if stress+data[0] > data[3]:
        stress-=data[2]
        if stress<0:
            stress=0
    else:
        work+=data[1]
        stress+=data[0]
    print(stress,work)
