## 공약수
'''
 아이디어 - 첫번째 n을 받을 때 밑의 숫자의 개수를 알 수 있다.
 n을 a b로 받아 놓으면 75 125 라는 숫자를 받는다.
 75 125 를 각각 소인수 분해한다.

 arr0의 ^(1/2) =< 
3=n 
66 11 3

66 33 22 11 6 3 2 1 11 1 3 1
 '''
import sys
sys.stdin = open('C:/Users/tcsss/Desktop/STUDY_CODE/solution/jlee14233/입력.txt','r')

n= list(map(int, input().split()))
data=list(map(int,input().split()))
for j in range(0,len(data)):
    g =[int(i) for i in range(1,int(int(data[j])**(1/2)+1)) if int(data[j])%i==0]
    k=[(int(int(data[j])/x)) for x in g if int(data[j])%x==0]
    data[j]=sorted(list(set(g+k)))

if n==[2]:
    gcd= sorted(list(set(data[0])&set(data[1])))
else:
    gcd = sorted(list((set(data[0])&set(data[1]))&set(data[2])))

print(*gcd, sep='\n')
