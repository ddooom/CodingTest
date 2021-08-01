# BJ 1181 단어 정렬 <정렬>
# https://www.acmicpc.net/problem/1181
# 시간 : 10
# 문제 리뷰 : E, P
# 회고 : 


n = int(input())
a =  sorted(list(set([input() for _ in range(n)])), key=(lambda x: (len(x), x)))
for w in a: print(w)