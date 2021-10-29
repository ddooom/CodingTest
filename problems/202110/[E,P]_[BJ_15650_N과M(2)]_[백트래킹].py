# BJ 15650 N과 M (2) <백트래킹>
# https://www.acmicpc.net/problem/15650
# 시간 : 10
# 문제 리뷰 : E,P
# 회고 : 


from itertools import combinations

N,M = map(int, input().split())
print('\n'.join(map(lambda x: ' '.join(map(str,x)), combinations([i for i in range(1,N+1)], M))))