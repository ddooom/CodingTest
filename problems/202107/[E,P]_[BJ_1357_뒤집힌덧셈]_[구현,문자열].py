# BJ 1357 뒤집힌 덧셈 <구현, 문자열>
# https://www.acmicpc.net/problem/1357
# 시간 : 5
# 문제 리뷰 : E, P
# 회고 : Pythonic하게 구현하기 편리했으며 난이도도 매우 쉬웠다.

a, b = input().split()
print(int(str(int(a[::-1])+int(b[::-1]))[::-1]))