# BJ 5639 이진 검색 트리 <그래프 이론, 그래프 탐색, 트리, 재귀>
# https://www.acmicpc.net/problem/5639
# 시간 : [경과 시간]
# 문제 리뷰 : [문제 리뷰]
# 회고 : [회고]

def tracking(root, nodes):
    sep_idx = len(list(filter(lambda x: x < root, nodes)))
    left = nodes[:sep_idx]
    right = nodes[sep_idx:]

    if len(left) > 0:
        G[root][0] = left[0]
        tracking(left[0], left[1:])
    if len(right) > 0:
        G[root][1] = right[0]
        tracking(right[0], right[1:])

def back(root):
    left = G[root][0]
    right = G[root][1]
    if left != 0:
        back(left)
    if right != 0:
        back(right)
    print(root)


import sys
sys.setrecursionlimit(100000)
N = list(map(int, [n[:-1] for n in sys.stdin.readlines()]))
G = {n: [0, 0] for n in N}

root = N[0]
tracking(root, N[1:])
back(root)