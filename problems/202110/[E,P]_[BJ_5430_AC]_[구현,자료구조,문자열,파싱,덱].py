# BJ 5430 AC <구현, 자료 구조, 문자열, 파싱, 덱>
# https://www.acmicpc.net/problem/5430
# 시간 : 20
# 문제 리뷰 : E,P
# 회고 : [회고]


from collections import deque

def solution(p, n, a):
    reverse = False
    for f in p:
        if f == 'R': reverse = True if not reverse else False

        if f == 'D':
            if n == 0:
                return 'error'

            if not reverse:
                a.popleft()
                n -= 1
            else:
                a.pop()
                n -= 1

    if reverse: 
        a.reverse()
    
    return f"[{','.join(a)}]"

for _ in range(int(input())):
    p = input()
    n = int(input())
    a = deque(input()[1:-1].split(','))
    print(solution(p,n,a))