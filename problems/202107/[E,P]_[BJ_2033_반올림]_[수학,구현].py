# BJ 2033 반올림 <수학, 구현>
# https://www.acmicpc.net/problem/2033
# 시간 : 10
# 문제 리뷰 : E, P
# 회고 : Other Answer은 10의 자리부터 올림을 수행, 따라서 길이가 길수록 복잡도가 크다
#        하지만 나의 코드는 수의 길이에 크게 영향을 받지 않는다.


n = input()
print(int(n) if len(n) == 1 else int(str(int(n[0])+1)+'0'*(len(n)-1)) if int(n[1:]) >= int('4'*(len(n)-2)+'5') else int(n[0]+'0'*(len(n)-1)))


''' Other Answer
n = int(input())
k = 10
while k < n:
    n=int(n/k+0.5)*k
    k*=10
print(n)
'''