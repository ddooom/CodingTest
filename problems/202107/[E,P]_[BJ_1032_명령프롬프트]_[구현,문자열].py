# BJ 1032 명령 프롬프트 <구현, 문자열>
# https://www.acmicpc.net/problem/1032
# 시간 : 10 min
# 문제 리뷰 : E, P
# 회고 : 첫 코딩테스트, 백준 입력을 어떻게 받아야하는지 찾는게 오래 걸렸다.


def solution(n, data):
    if n == 1:
        return data[0]

    answer = ''
    for i in range(len(data[0])):
        first = data[0][i]
        for j in range(1, n):
            if first != data[j][i]:
                answer += '?'
                break
            if j == n-1:
                answer += first
    return answer


n = int(input())
data = [input() for _ in range(n)]

print(solution(n, data))