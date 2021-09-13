# BJ 1012 유기농 배추 <그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색>
# https://www.acmicpc.net/problem/1012
# 시간 : 20
# 문제 리뷰 : M,R
# 회고 : 본인의 코드는 입력 받은 값을 리스트로 하여 거리가 1이면 리스트에서 해당 값을 없애고 스택에 넣어 깊이 우선 탐색을 하는 방식으로 구현
#        Faster Code는 입력 받은 값을 리스트로 처리하는 것이 아니라 실제 배추 밭처럼 N*M의 2차원 리스트로 하여 배추가 있으면 1을 넣음
#        그 후 1인 자리가 있으면 그 자리를 0으로 만들고 상하좌우에 있는 것을 다시 0으로 하게끔 재귀 함수를 구현하여 처리


import sys
input = sys.stdin.readline

def check_distance(a, b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2) == 1


for _ in range(int(input())):
    M,N,K = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(K)]
    
    answer = 0
    s = []
    while len(l) > 0:
        if len(s) == 0:
            s.append(l.pop(0))
            answer += 1
        
        i = 0
        while len(l) > i:
            if check_distance(s[0], l[i]):
                s.append(l.pop(i))
            else:
                i += 1
        s.pop(0)
    
    print(answer)


''' Faster Code
from sys import stdin, setrecursionlimit
setrecursionlimit(100000)
def dfs(maps, i, j):
    if maps[i][j] == 1:
        maps[i][j] = 0
        if i+1 < N and maps[i+1][j]==1:
            dfs(maps, i+1, j)
        if 0 <= i-1 and maps[i-1][j]==1:
            dfs(maps, i-1, j)
        if j+1 < M and maps[i][j+1]==1:
            dfs(maps, i, j+1)
        if 0 <= j-1 and maps[i][j-1]==1:
            dfs(maps, i, j-1)

for T in range(int(input())):
    N, M, K = map(int,stdin.readline().split())
    maps = [[0] * M for _ in range(N)]
    for _ in range(K):
        i, j = map(int, stdin.readline().split())
        maps[i][j] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 1:
                dfs(maps, i, j)
                cnt += 1
    print(cnt)
'''