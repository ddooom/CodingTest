# BJ 1259 팰린드롬수 <구현, 문자열>
# https://www.acmicpc.net/problem/1259
# 시간 : 10
# 문제 리뷰 : E, P
# 회고 : 다른 사람의 정답은 문자열의 길이만큼의 복잡도를 가지고 내
#        내 정답은 문자열 길이의 절반만큼의 복잡도를 가지지만 더 간단해보인다.
#        실행 시간은 같았다.
 

data = input()
while data != '0':
    print('yes' if all([data[i]==data[-1*(i+1)] for i in range(len(data)//2)]) else 'no')
    data = input()


''' Other`s Answer
while 1:
  s=input()
  if s=='0': break
  print('yes' if s==s[::-1] else 'no')
'''