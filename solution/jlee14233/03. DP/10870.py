## 피보나치 수 5
'''
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

'''
'''
DP 공부
DP란?
특정 범위까지의 값을 구하기 위해 이전 범위의 값을 활용하여 효율적으로 값을 얻는 기법.
이전 범위의 값을 저장하여, 똑같은 문제가 발생했을 때 이를 참조하여 해결한다.

사용의 상활
큰 문제를 해결하기 위해서 작은 문제로 쪼갰을 때, 작은 문제를 통해서 큰 문제의 답을 도출할 수 있을 경우
큰 문제를 해결하기 위해 작은 문제의 답을 여러번 구해야 할 경우

해결 방법
테이블을 정의 -> 점화식을 찾는다! -> 초기값 설정하기
이후 반복문을 돌려본다.

##메모이제이션 (memoization) 햐항식 프로그래밍
메모이제이션은 한번 계산한 결과를 메모리 공간에 메모하는 기법
같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져올 수 있다.
이 경우 시간 복잡도는 O(N)이 된다

##타뷸레이션 (tabulation) - 상향식 프로그래밍
메모이제이션과 비슷하나, 값을 미리 계산해두는 점이 다르다. 메모이제이션은 결과가 필요할 경우 계산하지만, 타뷸레이션은 필요하지 않는 값도 미리 계산해둔다는 차이가 발생한다. 이 경우 계산해둔 값은 시간복잡도가 O(1)상수시간이 되는 이점이 있다.

피보나치 수열의 문제는
재귀의 방식과, DP의 방식, 반복의 방식이 존재하게 된다.
재귀의 방식은 O(N^2)의 시간복잡도 DP의 방식은 O(N^2) 반복은 O(N)의 시간복잡도를 갖게 된다.

'''


import sys

sys.stdin = open('solution/jlee14233/03. DP/입력.txt', 'r')
n=int(sys.stdin.readline().strip())

def fibbo(n):
    d=[0]*(n+1)
    if n==1 or n==2:
        return 1
    if d[n]!=0:
        return d[n]
    d[n]=fibbo(n-1)+fibbo(n-2)
    return d[n]

print(fibbo(n))
