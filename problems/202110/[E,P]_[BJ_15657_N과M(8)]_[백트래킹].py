# BJ 15657 N과 M (8) <백트래킹>
# https://www.acmicpc.net/problem/15657
# 시간 : 10
# 문제 리뷰 : E,P
# 회고 : 


from itertools import combinations_with_replacement

N,M = map(int, input().split())
print('\n'.join(map(lambda x: ' '.join(map(str,x)), combinations_with_replacement(sorted(map(int,input().split())), M))))