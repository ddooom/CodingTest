# BJ 1356 유진수 <수학, 구현, 문자열, 사칙연산>
# https://www.acmicpc.net/problem/1356
# 시간 : 10
# 문제 리뷰 : E, P
# 회고 : 이번 문제는 난이도가 낮았으며 pythonic하게 한 줄 코딩을 시도하였다. 중간에 유진수를 만족하여도 반복문을 break하지 않아 시간복잡도에서는 효율적이지 않지만, 한 줄로도 가능했다.


num = list(map(int, input()))
answer = 'NO'
for i in range(len(num)-1):
    a = 1
    b = 1
    for n in range(i+1):
        a *= num[n]
    for m in range(i+1, len(num)):
        b *= num[m]
    if a == b:
        answer = 'YES'
        break
    print(num[:i+1], num[i+1:])

print(answer)


''' Custom Pythonic Code
from functools import reduce
num = list(map(int, input()))
print('YES' if any([reduce(lambda a, b: a*b, num[:i+1], 1)==reduce(lambda a, b: a*b, num[i+1:], 1) for i in range(len(num)-1)]) else 'NO')
'''