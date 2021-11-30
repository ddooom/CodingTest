# BJ 1629 곱셈 <수학, 분할 정복을 이용한 거듭제곱>
# https://www.acmicpc.net/problem/1629
# 시간 : 30
# 문제 리뷰 : M,R
# 회고 : 수학적으로 쉽게 풀어낼 수 있는 문제였다. 하지만 예외가 많아 오답이 많았다.
#        python에서 이 문제를 바로 해결해주는 pow라는 함수가 있었다. 수 두개를 넣으면 제곱을 해주지만 세개를 넣으면 제곱한 것을 나눠준다.


import math
A,B,C = map(int, input().split())
if C == 1:
    print(0)
else:
    compress = 1
    while B >= 1 and A > 1:
        times = math.ceil(math.log(C, A))
        compress *= A ** (B%times)
        A = A ** times % C
        B = B // times
    if A==0 and compress == 1:
        print(0)
    else:
        print(compress%C)


''' Pythonic Code
print(pow(*map(int,input().split())))
'''