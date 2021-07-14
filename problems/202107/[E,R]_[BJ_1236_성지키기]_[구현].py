# BJ 1236 성 지키기 <구현>
# https://www.acmicpc.net/problem/1236
# 시간 : 20
# 문제 리뷰 : E, R
# 회고 : Best Answer을 보면 sys를 저런식으로 받는 것이 더 빠르다. 
#        또한 all이나 any를 효율적으로 사용하였다. 


rowcol = [[n for n in range(nums)] for nums in map(int, input().split())]
data = [input() for _ in range(len(rowcol[0]))]
for r, row_v in enumerate(data):
    for c, v in enumerate(row_v):
        if v == 'X':
            if r in rowcol[0]: rowcol[0].remove(r)
            if c in rowcol[1]: rowcol[1].remove(c)

print(max(map(len, rowcol)))


''' Best Answer
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
x = [[i == '.' for i in input().rstrip()] for _ in range(n)]
s = sum(all(y) for y in zip(*x))
t = sum(all(y) for y in x)
print(max(s, t))
'''
