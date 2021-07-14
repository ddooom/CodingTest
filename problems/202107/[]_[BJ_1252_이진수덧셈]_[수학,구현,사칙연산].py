# BJ 1252 이진수 덧셈 <수학, 구현, 사칙연산>
# https://www.acmicpc.net/problem/1252
# 시간 : 30
# 문제 리뷰 : M, R
# 회고 : (Best Answer 참고) 십진수를 이진수로 변환하는 것 중 bin(value, 2)가 있었다.
#        int(value, 2)와 bin()를 이용하면 이진수 관련 문제를 간단하게 풀 수 있을 듯


ipt = input().split()
data = [b[::-1] + '0'*(max(map(len, ipt))-len(b)) for b in ipt]
p = 0

if '1' not in data[0] and '1' not in data[1]:
    print('0')

else:
    answer = ''
    for b1, b2 in zip(data[0], data[1]):
        if p == 0:
            if b1 != b2:
                answer += '1'
            else:
                answer += '0'
                if b1 == '1':
                    p = 1 
        else:
            if b1 != b2:
                answer += '0'
            else:
                answer += '1'
                if b1 == '0':
                    p = 0

    if p == 1:
        answer += '1'

    answer = answer[::-1]
    print(answer[answer.index('1'):])


''' Best Answer
x,y=[int(i,2)for i in input().split()]
print(bin(x+y)[2:])
'''