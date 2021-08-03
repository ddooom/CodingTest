# BJ 2108 통계학 <구현, 정렬>
# https://www.acmicpc.net/problem/2108
# 시간 : 50
# 문제 리뷰 : M, R
# 회고 : 내장 라이브러리의 효율성은 대단했다. 처음엔 Counter를 사용하지 않고 해보려 했으나 시간 초과 문제로 Counter를 사용했다.
#        Counter를 사용하니 채점된 문제가 늘어났고 다음으론 input() 대신 readline()을 사용하니 정답이 됐다.


from collections import Counter
import sys
input = sys.stdin.readline
l = sorted([int(input()) for _ in range(int(input()))])
c = Counter(l).most_common()
print(round(sum(l)/len(l)))
print(l[len(l)//2])
print(c[0][0] if (len(c) == 1 or c[0][1] != c[1][1]) else c[1][0])
print(l[-1]-l[0])
