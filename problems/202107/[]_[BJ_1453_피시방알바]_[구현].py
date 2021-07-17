# BJ 1453 피시방 알바 <구현>
# https://www.acmicpc.net/problem/1453
# 시간 : 5
# 문제 리뷰 : E, P
# 회고 : 창의력과 pythonic code만 있다면 한 줄로 해결 가능

n, data = input(), input().split()
print(len(data)-len(set(data)))

''' More Pythonic
print(int(input())-len(set(input().split())))
'''
