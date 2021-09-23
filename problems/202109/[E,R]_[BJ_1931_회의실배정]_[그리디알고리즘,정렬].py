# BJ 1931 회의실 배정 <그리디 알고리즘, 정렬>
# https://www.acmicpc.net/problem/1931
# 시간 : 15
# 문제 리뷰 : E,R
# 회고 : 요소가 리스트일 때, 리스트의 뒷 요소부터 정렬이 필요한 상황이라면 sorted(list, , key=lambda x: (x[1], x[0]))보단 
#        Faster Code처럼 [::-1]로 요소를 뒤집어 그냥 sorted(list)로 하면 효율적이다.


import sys
input = sys.stdin.readline

N = int(input())
L = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))

m = 1
s = L[0]
for i in range(1, len(L)):
    if s[1] <= L[i][0]:
        s = L[i]
        m += 1
        
print(m)


''' Faster Code
c = l = 0
for i, j in sorted([*map(int, q.split())][::-1]for q in[*open(0)][1:]):
 if j >= l: c += 1;l = i
print(c)
'''