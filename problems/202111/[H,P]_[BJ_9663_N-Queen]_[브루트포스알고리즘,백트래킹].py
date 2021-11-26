# BJ 9663 N-Queen <브루트포스 알고리즘, 백트래킹>
# https://www.acmicpc.net/problem/9663
# 시간 : 60 +
# 문제 리뷰 : H, P
# 회고 : 문제를 해결하지 못하여 찾아봤는데, 파이썬으로 백트래킹 문제는 효율적이지 않다고 한다.
#        애초에 빠른 언어가 아니기 때문인 것 같다. pypy3로도 시간 초과가 발생한다.


def possible(row_idx):
    for r in range(row_idx):
        if visit[r] == visit[row_idx] or abs(visit[row_idx] - visit[r]) == (row_idx - r):
            return False
    return True


def search(row_idx):
    global answer
    
    if row_idx == N:
        answer += 1
    
    else:
        for col_idx in range(N):
            visit[row_idx] = col_idx
            if possible(row_idx):
                search(row_idx + 1)


N = int(input())
visit = [0] * N
answer = 0
search(0)

print(answer)