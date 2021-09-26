# BJ 1074 Z <분할 정복, 재귀>
# https://www.acmicpc.net/problem/1074
# 시간 : 20
# 문제 리뷰 : M,R
# 회고 : 본인은 분할정복을 재귀 함수로 하여 문제를 해결하였다.
#        하지만 Best Pythonic Code는 행의 증가와 열의 증가의 규칙을 이진수 값을 사진수로 나타냄으로 찾아 한줄로 표현하였다... 대박


def solution(n, r, c, t):
    if n==0:
        return t
    if r<(2**(n-1)) and c<(2**(n-1)):
        return solution(n-1, r, c, t)
    elif r<(2**(n-1)) and c>=(2**(n-1)):
        return solution(n-1, r, c-2**(n-1), t+2**(2*(n-1)))
    elif r>=(2**(n-1)) and c<(2**(n-1)):
        return solution(n-1, r-2**(n-1), c, t+2*2**(2*(n-1)))
    else:
        return solution(n-1, r-2**(n-1), c-2**(n-1), t+3*2**(2*(n-1)))
    
N,r,c=map(int,input().split())
print(solution(N,r,c,0))


''' Best Pythonic Code
n,r,c=map(int,input().split());print(int(f'{c:b}',4)+2*int(f'{r:b}',4))
'''