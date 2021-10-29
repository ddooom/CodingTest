# BJ 15654 N과 M (5) <백트래킹>
# https://www.acmicpc.net/problem/15654
# 시간 : 10
# 문제 리뷰 : E,P
# 회고 : 


from itertools import permutations

N,M = map(int, input().split())
print('\n'.join(map(lambda x: ' '.join(map(str,x)), permutations(sorted(map(int,input().split())), M))))