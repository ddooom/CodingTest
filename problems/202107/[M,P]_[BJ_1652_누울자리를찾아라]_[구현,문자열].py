# BJ 1652 누울 자리를 찾아라 <구현, 문자열>
# https://www.acmicpc.net/problem/1652
# 시간 : 20
# 문제 리뷰 : M, P
# 회고 : Pythonic하게 해결하려고 노력했지만 한 줄 코딩이라기엔 너무 긴 코드가 되었다. 
#        '..' 이든 '.........' 이든 1로 표현해야 하는데 맞은 사람을 보니 정규표현식을 많이 사용했다.


import sys
input = sys.stdin.readline
n = int(input())
data = [list(input().rstrip()) for _ in range(n)]
print(sum([(''.join(row).index('X')>=2)+(''.join(row).count('X..')) if 'X' in row else 1 if len(row)>=2 else 0 for row in data]), \
    sum([(''.join(col).index('X')>=2)+(''.join(col).count('X..')) if 'X' in col else 1 if len(col)>=2 else 0 for col in zip(*data)]))


