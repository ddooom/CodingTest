# BJ 1145 적어도 대부분의 배수 <브루트포스 알고리즘>
# https://www.acmicpc.net/problem/1145
# 시간 : 30
# 문제 리뷰 : M, R
# 회고 : 정답이 맞아도 float 형인가 int 형인가에 따라 오답이 될 수 있었다.
#        이 외에도 answer를 1씩 올려가며 대부분의 배수를 찾는 것도 솔루션이 될 수 있었다. 훨씬 느리지만


def gcd(a, b):
    return b if a == 0 else gcd(b%a,a)

def lcm(a, b):
    return a*b//gcd(a,b)

data = list(map(int, input().split()))

answer = []
for i in range(len(data)):
    for j in range(i+1, len(data)):
        for k in range(j+1, len(data)):
            answer.append(lcm(lcm(data[i], data[j]), data[k]))

print(min(answer))


'''
data = list(map(int, input().split()))
correct = 0
answer = 2

while correct != 3:
    correct = 0
    for n in data:
        if answer % n == 0:
            correct += 1
        if correct == 3:
            break
    answer += 1

print(answer-1)
'''
