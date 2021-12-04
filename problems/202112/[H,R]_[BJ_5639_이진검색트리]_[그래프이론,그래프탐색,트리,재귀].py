# BJ 5639 이진 검색 트리 <그래프 이론, 그래프 탐색, 트리, 재귀>
# https://www.acmicpc.net/problem/5639
# 시간 : 60+
# 문제 리뷰 : H,R
# 회고 : 전위 순회 결과는 루트를 기준으로 두개의 서브 트리로 나뉘어 출력된 다는 것을 이용하여
#       루트 기준으로 나눠지는 서브 트리의 인덱스를 구하였고 이를 다시 재귀 하였다.
#       서브 트리가 루트 밖에 없으면 이를 왼쪽부터 출력하게 하여 그래프를 구성하여 다시 후위 순회 출력이 아닌 재귀 내에서 정답이 출력되도록 하였다.


def tracking(root, start_idx, end_idx):
    sep_idx = start_idx + len(list(filter(lambda x: x < root, N[start_idx:end_idx+1])))
    
    if sep_idx > start_idx+1:
        tracking(N[start_idx], start_idx+1, sep_idx-1)
    elif sep_idx - start_idx == 1:
        print(N[start_idx])

    if end_idx > sep_idx:
        tracking(N[sep_idx], sep_idx+1, end_idx)
    elif end_idx - sep_idx == 0:
        print(N[sep_idx])
    
    print(root)


import sys
sys.setrecursionlimit(100000)
N = list(map(int, [n[:-1] for n in sys.stdin.readlines()]))

root = N[0]
tracking(root, 1, len(N)-1)