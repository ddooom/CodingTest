# BJ 1676 팩토리얼 0의 개수 <수학>
# https://www.acmicpc.net/problem/1676
# 시간 : 10
# 문제 리뷰 : E, R
# 회고 : 정공법으로 풀이하면 쉬운 문제, 하지만 문제 유형은 '수학'이다.
#        입력받은 수가 a라고 하면 정답은 a//5**3+a//5**2+a//5가 되는데, 그 이유는 factorial에서 끝의 0의 개수는 약수들 중 5의 개수이기 때문이다.
#        그 이유는 10이 0의 개수이나 10의 약수는 2,5이고 2는 무조건 5의 수보다 많기 때문이다.
#        따라서 약수가 5일 경우 0의 수는 1, 5**2일 경우 0의 수는 2가 더해지는 것이다.


fac = 1
for i in range(1, int(input())+1):
    fac *= i

ans = 0
while 1:
    if fac % (10**i) != 0: break
    ans+=1
print(ans-1)


''' My Answer Using Math Library
import math
f = str(math.factorial(int(input())))
print(len(f)-len(f.rstrip('0')))
'''


''' Best Answer
a=int(input())//5
print(a//25+a//5+a)
'''