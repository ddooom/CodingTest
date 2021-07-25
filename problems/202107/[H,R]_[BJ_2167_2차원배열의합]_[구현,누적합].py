# BJ 2167 2차원 배열의 합 <구현, 누적합>
# https://www.acmicpc.net/problem/2167
# 시간 : 30
# 문제 리뷰 : H, R
# 회고 : 이전에는 sum을 두 번 사용하여 입력받은 인덱스 내의 합을 구했으나 시간 초과
#        따라서 입력을 받음과 동시에 해당 인덱스 이전 요소의 누적합을 요소로 하는 2차원 배열 생성
#        i, j, x, y를 입력받으면 누적합이 기록된 arr에서 arr[x][y] - arr[x][j-1] - arr[i-1][y] + arr[i-1][j-1]를 통해 부분합을 구함


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0] * (m+1)]
for _ in range(n):
    ipt = [0] + list(map(int, input().split()))
    for i, v in enumerate(ipt[1:]):
        ipt[i+1] = ipt[i] + v + arr[-1][i+1] - arr[-1][i]
    arr.append(ipt)

it = int(input())
for _ in range(it):
    i, j, x, y = map(int, input().split())
    print(arr[x][y] - arr[x][j-1] - arr[i-1][y] + arr[i-1][j-1])