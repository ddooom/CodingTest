# BJ 17626 Four Squares <다이나믹 프로그래밍, 브루트포스 알고리즘>
# https://www.acmicpc.net/problem/17626
# 시간 : 30
# 문제 리뷰 : M, R
# 회고 : 내 코드와 Faster Code 모두 답이 1일 때, 2일 때 순으로 검사하고 출력한다.
#        하지만 내 코드는 하나의 값을 모두 계산하고 리스트에 저장하지만 Faster Code는 값 하나하나를 계산하고 검사하기 때문에 더 빠른 것 같다.


def sub_times(n):
    ls = []
    for i in range(int((n/2)**.5), int((n)**.5)+1):
        ls.append(n-i**2)
    return ls

def solution(n):
    ls = [n]
    ans = 0
    while 1:
        sub = []
        ans += 1
        for n in ls:
            sub_ls = sub_times(n)
            if 0 in sub_ls:
                return ans
            sub.extend(sub_times(n))
        ls = sub
        
print(solution(int(input())))


''' Faster Code
from math import sqrt

def rrange(n):
    return (q ** 2 for q in range(int(sqrt(n // 2)), int(sqrt(n)) + 1))

def simulate(n):
    squares = [rn ** 2 for rn in range(1, int(sqrt(n)) + 1)]

    if n in squares:
        return 1
    
    for s in rrange(n):
        if n - s in squares:
            return 2
            
    for s in rrange(n):
        nn = n - s
        for t in rrange(nn):
            if n - s - t in squares:
                return 3

    return 4

n = int(input())

print(simulate(n))
'''