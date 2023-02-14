## four squares
'''
문제
라그랑주는 1770년에 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다고 증명하였다. 어떤 자연수는 복수의 방법으로 표현된다. 예를 들면, 26은 52과 12의 합이다; 또한 42 + 32 + 12으로 표현할 수도 있다. 역사적으로 암산의 명수들에게 공통적으로 주어지는 문제가 바로 자연수를 넷 혹은 그 이하의 제곱수 합으로 나타내라는 것이었다. 1900년대 초반에 한 암산가가 15663 = 1252 + 62 + 12 + 12라는 해를 구하는데 8초가 걸렸다는 보고가 있다. 좀 더 어려운 문제에 대해서는 56초가 걸렸다: 11339 = 1052 + 152 + 82 + 52.

자연수 n이 주어질 때, n을 최소 개수의 제곱수 합으로 표현하는 컴퓨터 프로그램을 작성하시오.

입력
입력은 표준입력을 사용한다. 입력은 자연수 n을 포함하는 한 줄로 구성된다. 여기서, 1 ≤ n ≤ 50,000이다.

출력
출력은 표준출력을 사용한다. 합이 n과 같게 되는 제곱수들의 최소 개수를 한 줄에 출력한다.
'''

import sys
import math

def squares(n):
    tab=[i**2 for i in range(224)]
    sq_list=[0]*4
    temp=int(math.sqrt(n))
    while n!=sum(sq_list):
        m=n
        sq_list[0]=temp
        m=m-tab[temp]
        print(tab[temp],m)
        for i in range(1,4):
            if m==0:
                return sq_list
            else:
                t=int(math.sqrt(m))
                m=m-t**2
                sq_list[i]=t
        print(sq_list)
        
        temp-=1
    return sq_list

print(squares(11339))
'''
문제를 푸는 방식을 이해했음.
내일 수정해야할 것
sq[0][1][2][3] 의 범위를 설정해야함, 무조건적으로 내림차순으로 나타날 수 있도록 만들어야함.
for 문을 여러개를 돌리는 이유를 알게 되었음.
3456 같이 운좋게 아다리 맞으니까] 16 56 8 2 이런 숫자가 나타남.
아다리가 하나도 맞지 않은 34567의 숫자는 에러가 발생하게 됨.
또한 근사치를 보여줄 뿐이고 제대로 된 정답은 나타나지 않음.
아다리가 진짜 개좋게 맞아야지 0으로 떨어지는 숫자를 보냄.
'''
