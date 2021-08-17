# BJ 1620 나는야포켓몬마스터이다솜 <자료 구조, 해시를 사용한 집합과 맵>
# https://www.acmicpc.net/problem/1620
# 시간 : 15
# 문제 리뷰 : E, P
# 회고 : 모두 dictionary로 했지만, dictionary와 list를 같이 쓴다면 더 빠를 것이다.


import sys
input = sys.stdin.readline

N,M = map(int, input().split())
d = {}

for i in range(N):
    a = input().rstrip()
    n = str(i+1)
    d[n] = a
    d[a] = n
print(d)

for _ in range(M):
    print(d[input().rstrip()])