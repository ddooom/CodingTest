# BJ 1526 가장 큰 금민수 <수학>
# https://www.acmicpc.net/problem/1526
# 시간 : 20
# 문제 리뷰 : M, R
# 회고 : 조건에 맞춰 나올 수 있는 경우의 수를 뽑는 여러 방법을 배웠다.
#        무엇보다 주어진 숫자로 나올 수 있는 수를 찾는데엔 
#        Best Answer처럼 이진수나 n진수를 사용하는 것이 매우 효율적이었다.


num = input()

if int(num) < int('4'*len(num)):
    print(int('7'*(len(num)-1)))
else:
    answer = ['4']*len(num)
    for i in range(len(num)):
        temp = answer.copy()
        temp[i] = '7'
        if int(num) // int("".join(temp)) > 0:
            answer[i] = '7'

    print(int("".join(answer))) 


''' Best Answer
g=lambda n:int(''.join(map(lambda i:'47'[int(i)],bin(n+1)[3:])))
i,k=0,int(input())
while g(i+1)<=k:i+=1
print(g(i))
'''



