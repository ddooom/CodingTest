# BJ 11053 가장 긴 증가하는 부분 수열 <다이나믹 프로그래밍>
# https://www.acmicpc.net/problem/11053
# 시간 : 20
# 문제 리뷰 : M,R
# 회고 : 


N = int(input())
L = list(map(int, input().split()))

max_len_list = [1]
for i in range(1, N):
    
    len_list = []
    for j in range(i):
        if L[j] < L[i]:
            len_list.append(max_len_list[j] + 1)
        else:
            len_list.append(1)
    
    max_len_list.append(max(len_list))

print(max(max_len_list))