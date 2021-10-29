# BJ 15652 N과 M (4) <백트래킹>
# https://www.acmicpc.net/problem/15652
# 시간 : 10
# 문제 리뷰 : E,P
# 회고 : 


from itertools import combinations_with_replacement

N,M = map(int, input().split())
print('\n'.join(map(lambda x: ' '.join(map(str,x)), combinations_with_replacement([i for i in range(1,N+1)], M))))