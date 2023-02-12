## 괄호의 값
'''
문제
4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서 올바른 괄호열이란 다음과 같이 정의된다.

한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다.
만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다.
X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.
예를 들어 ‘(()[[]])’나 ‘(())[][]’ 는 올바른 괄호열이지만 ‘([)]’ 나 ‘(()()[]’ 은 모두 올바른 괄호열이 아니다. 우리는 어떤 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을 아래와 같이 정의하고 값(X)로 표시한다.

‘()’ 인 괄호열의 값은 2이다.
‘[]’ 인 괄호열의 값은 3이다.
‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
예를 들어 ‘(()[[]])([])’ 의 괄호값을 구해보자. ‘()[[]]’ 의 괄호값이 2 + 3×3=11 이므로 ‘(()[[]])’의 괄호값은 2×11=22 이다. 그리고 ‘([])’의 값은 2×3=6 이므로 전체 괄호열의 값은 22 + 6 = 28 이다.

여러분이 풀어야 할 문제는 주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산하여 출력하는 것이다.

입력
첫째 줄에 괄호열을 나타내는 문자열(스트링)이 주어진다. 단 그 길이는 1 이상, 30 이하이다.

출력
첫째 줄에 그 괄호열의 값을 나타내는 정수를 출력한다. 만일 입력이 올바르지 못한 괄호열이면 반드시 0을 출력해야 한다.


문자열로 접근한다면 replace('[]','',1)이걸로 하면 되려나?

스택으로 접근해본다.
(를 읽는다 다음에 나오는 문자가 (,[의 경우 
operation 스택에 2x를 저장한다
) 가 나올 경우 (2+를 저장한다
[는 위와 동일하다 3으로만 변경
)를 읽고 난 다음의 문자가 [,( 일 경우 +(를 저장하고 넘어간다
))의 경우 계산을 한다. )를 남긴다
(()[[]])([])
시작 ( 이므로 스택에 저장한다
(이후에 (가 나오기 때문에 oper스택에 2x를 저장한다
((이후 )가 출력되므로 (2+를 oper스택에 저장한다
(()[ 이므로 넘어간다
x2+2(
(([[
x2+2(x3
(([[]
x2+2(x3+3
(([[]])
x2(+2(x3(+3)))
(([[]])(
x2(+2(x3(+3)))(
(([[]])([
x2(+2(x3(+3)))(x2
(([[]])([])
x2(+2(x3(+3)))+(x2(+3))
위와 같이 계산을 그대로 하면 됨.
while문으로 괄호가 정상적이지 않을 경우에는 0를 출력한다 (replace를 활용하면 될 듯 )
2개의 or문으로 처리하니까 쌉가능.

eval(2*(2+(3*(+3)))+(2*(+3))
괄호가 정상적이지 않을 경우를 어떻게 거시기 해야할지 (해결함)
괄호제거 문제 가져오기
n = int(input())

    words = input()

    while '()' in words:
        words = words.replace('()', '')

    if len(words):
        print('NO')
    else:
        print('YES')

'''
import sys
sys.stdin = open('solution/jlee14233/02. data_structure/입력.txt', 'r')
words = sys.stdin.readline().strip()
stack=[]
oper=[]

test=words
while '()' in test or '[]' in test:
    test =test.replace('()','').replace('[]','')
if test!='':
    print(0)
    quit()
'''

0의 경우에 가장 words의 가장 첫 문자  word[0]를 스택에 저장한다
stack[-1]와 word[i]을 비교한다
stack[-1]이 (일 경우에 words[i]가 )
이면
oper에 (+2를 저장한다
word[i]가 ([일 경우
2*(로 저장한다
stack[-1]이 ) 일 경우에 word[i]가 (,[일 경우
oper에 )+를 저장한다
word[i]가 ),] 일 경우)를 저장한다

'''
for i in range(len(words)):
    if i==0:
        stack.append(words[0])
    elif words[i]=='(':
        if stack[-1]=='(': 
            oper.append('2*(')
            stack.append(words[i])
        elif stack[-1]=='[':
            oper.append('3*(')
            stack.append(words[i])
        elif stack[-1]==')' or stack[-1]==']':
            oper.append(')+')
            stack.append(words[i])
    elif words[i]==')':
        if stack[-1]=='(' or stack[-1]=='[':
            oper.append('(+2')
            stack.append(words[i])
        elif stack[-1]==')' or stack[-1]==']':
            oper.append(')')
            stack.append(words[i])
    elif words[i]=='[':
        if stack[-1]=='(':
            oper.append('2*(')
            stack.append(words[i])            
        elif stack[-1]=='[':
            oper.append('3*(')
            stack.append(words[i])
        elif stack[-1]==']' or stack[-1]==')':
            oper.append(')+')
            stack.append(words[i])
    elif words[i]==']':
        if stack[-1]=='[' or  stack[-1]=='(':
            oper.append('(+3')
            stack.append(words[i])
        elif stack[-1]==')' or stack[-1]==']':
            oper.append(')')
            stack.append(words[i])
oper.append(')')
k=''.join(map(str,oper))
print(eval(k))

'''
쇠막대기 문제 가져오기
컨셉은 이거와 유사한데 product 계산을 어떻게 진행해야할지? 그 문제가 생김.

cnt=0
stack=[]
words = list(sys.stdin.readline())

for i in range(len(words)):    
    if words[i]=='(':
        stack.append('(')
    else:
        if words[i-1]=='(':
            stack.pop()
            cnt+=len(stack)
        else:
            stack.pop()
            cnt+=1
print(cnt)

위의 문제를 깨달았다. 부분적으로 틀리게 계산이 들어가는 경우가 발생했음.
서순차이를 다시 보고 만드니까 됐다. 괄호의 순서를 어떻게 넣냐에 따라 답이 매우 달라졌음.
그렇다면 계산을 result로 결정해서 들어가야 하는게 맞음. eval을 이용하는 방법

'''