# BJ 9663 N-Queen <브루트포스 알고리즘, 백트래킹>
# https://www.acmicpc.net/problem/9663
# 시간 : [경과 시간]
# 문제 리뷰 : [문제 리뷰]
# 회고 : [회고]

def marking(row_idx, col_idx, visit):
    for i in range(N):
        visit[row_idx][i] = True
        visit[i][col_idx] = True
        if 0<=(row_idx + i*1)<N and 0<=(col_idx + i*1)<N:
            visit[row_idx + i*1][col_idx + i*1] = True
        if 0<=(row_idx - i*1)<N and 0<=(col_idx + i*1)<N:
            visit[row_idx - i*1][col_idx + i*1] = True
        if 0<=(row_idx + i*1)<N and 0<=(col_idx - i*1)<N:
            visit[row_idx + i*1][col_idx - i*1] = True
        if 0<=(row_idx - i*1)<N and 0<=(col_idx - i*1)<N:
            visit[row_idx - i*1][col_idx - i*1] = True
    return visit


def search(row_idx, col_idx, visit):
    global answer
#     for i in range(N):
#         print(visit[i])
#     print()
    if row_idx == (N-1):
        answer += 1
        return 0
    
    if col_idx-2 >= 0:
        for i in range(col_idx-2, -1, -1):
            if not visit[row_idx+1][i]: 
                tmp_visit = visit.copy()
                tmp_visit = marking(row_idx+1, i, tmp_visit)
                search(row_idx+1, i, tmp_visit)
    
    if col_idx+2 < N:
        for i in range(col_idx+2, N):
            if not visit[row_idx+1][i]:
                tmp_visit = visit.copy()
                tmp_visit = marking(row_idx+1, i, tmp_visit)
                search(row_idx+1, i, tmp_visit)
    

N = int(input())
answer = 0
for col_idx in range(N):
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit = marking(0, col_idx, visit)
    search(0, col_idx, visit)

print(answer)