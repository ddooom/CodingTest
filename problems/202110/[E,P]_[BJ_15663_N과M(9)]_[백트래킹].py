# BJ 15663 N과 M(9) <백트래킹>
# https://www.acmicpc.net/problem/15663
# 시간 : 25
# 문제 리뷰 : E,P
# 회고 :


from itertools import permutations

N,M = map(int, input().split())
print('\n'.join(map(lambda x:' '.join(map(str,x)),sorted(list(set(permutations(map(int,input().split()), M))),key=lambda x:[x[i] for i in range(M)]))))