## 에너지 드링크
'''
문제
페인은 에너지 드링크를 좋아하는 회사원이다. 에너지 드링크는 카페인, 아르기닌, 타우린, 나이아신 등의 성분이 들어있어 피로 회복에 도움을 주는 에너지 보충 음료수이다.

야근을 마치고 한밤중에 퇴근하니 벌써 새벽 1시. 하지만 주말은 아직 멀었고, 다음 날에도 정시에 출근해야 하는 페인은 오늘도 에너지 드링크를 찾는다.

반복되는 야근에 지친 나머지, 평소보다 더 많은 에너지와 피로 회복이 필요했던 페인은 집에 있던 에너지 드링크들을 한 데 합쳐서, 하나의 에너지 드링크로 만들어 한번에 마시려 한다.

페인이 에너지 드링크들을 합치는 과정은 다음과 같다.

임의의 서로 다른 두 에너지 드링크를 고른다.
한쪽 에너지 드링크를 다른 쪽 에너지 드링크에 모두 붓는다. 단, 페인은 야근 후유증으로 인해 손이 떨려, 붓는 과정에서 원래 양의 절반을 바닥에 흘리게 된다.
다 붓고 남은 빈 에너지 드링크는 버린다.
1~3 과정을 에너지 드링크가 하나만 남을 때까지 반복한다.
예를 들어, 두 에너지 드링크 a, b가 있고, 양이 각각 xa, xb라 할 때, 다음 둘 중 하나의 선택을 할 수 있다.

a의 양을 xa + (xb / 2)로 만들고, b를 버리기
b의 양을 xb + (xa / 2)로 만들고, a를 버리기
페인은 합쳐진 에너지 드링크의 양을 최대로 하려 한다. 불쌍한 페인을 도와주자!

입력
첫째 줄에 페인이 가지고 있는 에너지 드링크의 수 N이 주어진다. (2 ≤ N ≤ 105)

둘째 줄에 각 에너지 드링크의 양이 공백으로 구분되어 주어진다. i번째 정수 xi (1 ≤ xi ≤ 109)는 에너지 드링크 i의 양이 xi임을 의미한다.

출력
첫째 줄에 페인이 최대로 만들 수 있는 에너지 드링크의 양을 출력한다.

절대/상대 오차는 10-5까지 허용한다.
'''


import sys
from collections import deque

sys.stdin = open('solution/jlee14233/08. Greedy/입력.txt', 'r')


n=int(sys.stdin.readline())

energy=deque(sorted(map(int,sys.stdin.readline().strip().split()),reverse=True))

def sum_energy(n):
    res_1=deque.popleft(n)
    sum_drink=0
    while n:
        res_2=deque.popleft(n)
        if res_1>res_2:
            sum_drink=res_1+(res_2*0.5)
        else:
            sum_drink=res_2+(res_1*0.5)
        res_1=sum_drink
    return sum_drink

print(sum_energy(energy))
