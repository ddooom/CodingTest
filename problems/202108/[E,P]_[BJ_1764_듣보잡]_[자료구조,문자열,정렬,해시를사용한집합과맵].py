# BJ 1764 듣보잡 <자료 구조, 문자열, 정렬, 해시를 사용한 집합과 맵>
# https://www.acmicpc.net/problem/1764
# 시간 : 10
# 문제 리뷰 : E, P
# 회고 : 


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n = set([input().rstrip() for _ in range(N)])
m = set([input().rstrip() for _ in range(M)])
ans = sorted(list(n&m))
print(len(ans))
print('\n'.join(ans))