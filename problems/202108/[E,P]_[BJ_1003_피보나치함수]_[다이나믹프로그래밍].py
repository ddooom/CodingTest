# BJ 1003 피보나치 함수 <다이나믹 프로그래밍>
# https://www.acmicpc.net/problem/1003
# 시간 : 10
# 문제 리뷰 : E, P
# 회고 : 범위가 정해져있어 40까지 미리 계산해놓았지만 아닌 경우, 미리 입력을 받고 입력받은 수 중 가장 큰 수까지를 범위로 해도 될 듯하다.


z = [1, 0]
o = [0, 1]
for _ in range(38):
    o.append(o[-1]+o[-2])
    z.append(z[-1]+z[-2])

for _ in range(int(input())):
    n = int(input())
    print(z[n], o[n])