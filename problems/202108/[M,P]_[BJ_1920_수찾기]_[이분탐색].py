# BJ 1920 수 찾기 <이분탐색>
# https://www.acmicpc.net/problem/1920
# 시간 : 20
# 문제 리뷰 : M, P
# 회고 : a in b 형식으로 수를 찾으면 시간복잡도는 리스트의 길이이다. 따라서 이분 탐색 함수를 정의하여 문제를 빠르게 풀이하였다.
#       처음에는 재귀 함수 형식과 리스트를 슬라이싱하여 이분 탐색을 하였지만, 시간 초과가 일어나 인덱스를 통해 이분 탐색을 하였다.
#       인덱스로 접근하는 것이 가장 빠르다는 것을 알게 되었다.


def BinarySearch(target, list):
    s, e = 0, len(list)-1
    while 1:
        m = (e-s)//2+s
        if s > e: return 0
        elif list[m] == target: return 1
        elif list[m] < target: s = m+1
        else: e = m-1


n, l = input(), sorted(list(map(int, input().split())))
n, i = input(), list(map(int, input().split()))
for t in i:
    print(BinarySearch(t, l))

