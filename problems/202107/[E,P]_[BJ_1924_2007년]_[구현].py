# BJ 1924 2007년 <구현>
# https://www.acmicpc.net/problem/1924
# 시간 : 10
# 문제 리뷰 : E, P
# 회고 : datetime 라이브러리를 사용했다면 더욱 쉽게 풀 수 있는 문제

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

m, d = map(int, input().split())
print(weeks[(sum(days[:m])+d)%7-1])