##투에-모스 문자열
'''
문제
0과 1로 이루어진 길이가 무한한 문자열 X가 있다. 이 문자열은 다음과 같은 과정으로 만들어진다.

X는 맨 처음에 "0"으로 시작한다. 
X에서 0을 1로, 1을 0으로 뒤바꾼 문자열 X'을 만든다.
X의 뒤에 X'를 붙인 문자열을 X로 다시 정의한다. 
2~3의 과정을 무한히 반복한다.
즉, X는 처음에 "0"으로 시작하여 "01"이 되고, "0110"이 되고, "01101001"이 되고, ⋯ 의 과정을 거쳐 다음과 같이 나타내어진다.

    "011010011001011010010110011010011001011001101001⋯⋯"

자연수 k가 주어졌을 때 X의 k번째에는 무슨 문자가 오는지 구하여라.

입력
첫 번째 줄에 자연수 k (1 ≤ k ≤ 1018) 가 주어진다.

출력
첫 번째 줄에 k번째에 오는 문자를 출력하라.

풀이 실패

'''

x='0'
y='1'
cnt=0
result=x+y
INF=59
'''
while cnt<6:
    if cnt%2==0:
        result = result+result[::-1]
    else:
        result = result+result[cnt::-1]+result[:cnt:-1]
    cnt+=1

    print(result)
'''

'''

0110 1001
0110 1001 1001 0110
0110 1001 1001 0110 1001 0110 0110 1001
0110 1001 1001 0110 1001 0110 0110 1001 1001 0110 0110 1001 0110 1001 1001 1001 0110

0110 1001 1001 0110 1001 0110 0110 1001 1001 0110 0110 1001
a=0110
b=1001
a b b a b a a b b a a b a b b a
0110 1001
abba baab 4
xyyx yxxy 16
ijji jiij 64
1221 2112 256
tsst stts 1024

x=abba(16개를 포함함)
y=baab
xyyx yxxy 
i=xyyx 4^3
j=yxxy 4^3

16번째 = x의 a의 마지막이므로 0
17번째 =xy에서 y의 시작점이므로 y=baab, b=1001, 1
32번째 = y의 b의 마지막이므로 1

나머지로 계산하는 것 같은데 어떤 방식인지 조금 더 고민해보기

100/64 = 1+ 36
36/16 = 2 + 4
4/4 = 1 + 0
i y a

'''