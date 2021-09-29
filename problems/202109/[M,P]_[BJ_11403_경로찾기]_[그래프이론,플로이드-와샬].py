# BJ 11403 경로 찾기 <그래프 이론, 플로이드-와샬>
# https://www.acmicpc.net/problem/11403
# 시간 : 15
# 문제 리뷰 : M,P
# 회고 : 재귀를 이용한 DFS


def search(n): 
    if v[n] == 0:
        v[n] = 1
        for x in G[n]:
            search(x)

N = int(input())
G = {i:[j for j,n in enumerate(input().split()) if n=='1'] for i in range(N)}

for i in range(N):
    v = [0] * N
    for x in G[i]:
        search(x)
    print(' '.join(map(str,v)))