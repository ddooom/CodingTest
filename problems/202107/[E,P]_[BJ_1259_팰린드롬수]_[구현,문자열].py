# BJ 1259 팰린드롬수 <구현, 문자열>
# https://www.acmicpc.net/problem/1259
# 시간 : [경과 시간]
# 문제 리뷰 : [문제 리뷰]
# 회고 : [회고]

data = input()
while data != '0':
    print('yes' if all([data[i]==data[-1*(i+1)] for i in range(len(data)//2)]) else 'no')
    data = input()