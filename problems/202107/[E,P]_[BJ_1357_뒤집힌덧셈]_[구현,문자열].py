# BJ 1357 뒤집힌 덧셈 <구현, 문자열>
# https://www.acmicpc.net/problem/1357
# 시간 : [경과 시간]
# 문제 리뷰 : [문제 리뷰]
# 회고 : [회고]

a, b = input().split()
print(str(int(a[::-1])+int(b[::-1]))[::-1])