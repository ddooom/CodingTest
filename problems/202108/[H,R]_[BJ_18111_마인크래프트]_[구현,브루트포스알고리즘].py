# BJ 18111 마인크래프트 <구현, 브루트포스 알고리즘>
# https://www.acmicpc.net/problem/18111
# 시간 : 60
# 문제 리뷰 : H, R
# 회고 : 처음으로 아예 못 풀겠어서 풀이를 찾아본 문제이다.
#        처음에는 반복문의 범위 문제인 줄 알고 범위를 줄이려고 하였다. 그 결과 min(0)부터 (sum(ls) + B) // len(ls)까지의 범위로 줄일 수 있었다.
#        하지만 범위가 문제가 아니였다. 이전 코드에서는 수많은 sum, min, map, filter로 긴 리스트의 접근을 많이 허용하였다.
#        정답이 된 풀이의 공통점은 중첩된 값을 다른 리스트로 표현했다는 것이다.
#        첫번째 코드에서는 blocks로 h별 개수를 저장하여 효율적으로 접근하였고 두번째 코드는 dictionary를 통해 접근하였다.
#        이런 구현 문제에서는 반복문의 범위도 중요하겠지만, 리스트의 최대 길이를 생각하여 이 리스트의 값들을 어떻게 다르게 나타낼 수 있을까를 생각해야겠다.


import sys

N, M, B = list(map(int, sys.stdin.readline().strip().split()))
ls = []
for _ in range(N):
    ls += list(map(int, sys.stdin.readline().strip().split()))

h_upper = (sum(ls) + B) // len(ls)

blocks = [0] * 257
for i in ls:
    blocks[i] += 1

time = 256 * 500 * 500 * 2
height = 0
for h in range(h_upper + 1):
    t = 0
    for i in range(257):
        if i < h:
            t += blocks[i] * (h - i)
        else:
            t += blocks[i] * (i - h) * 2
    if t <= time:
        time = t
        height = h
print(time, height)


''' dictionary를 사용한 풀이
import sys
from collections import defaultdict

input = sys.stdin.readline

N, M, B = map(int, input().split())
dic = defaultdict(int)

for i in range(N):
    for j in list(map(int, input().split())):
        dic[j] += 1

key = list(dic.keys())

min_value = min(key)
max_value = max(key)

min_count = int(1e9)
h = 0

for x in range(min_value, max_value + 1):
    count, have = 0, B
    for y in dic.keys():
        if x > y:
            count += (x - y) * dic[y]
            have -= (x - y) * dic[y]
        elif x < y:
            count += 2 * (y - x) * dic[y]
            have += (y - x) * dic[y]

    if have >= 0:
        min_count = min(min_count, count)
        if min_count == count:
            h = x
print(min_count, h)
'''