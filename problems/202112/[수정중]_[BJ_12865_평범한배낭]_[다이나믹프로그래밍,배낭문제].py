# BJ 12865 평범한 배낭 <다이나믹 프로그래밍, 배낭 문제>
# https://www.acmicpc.net/problem/12865
# 시간 : 
# 문제 리뷰 : [문제 리뷰]
# 회고 : [회고]


from collections import deque

N, K = map(int, input().split())
weight2value = {}
for i in range(N):
    weight, value = map(int, input().split())
    weight2value[weight] = value

weights = set(weight2value.keys())

queue = deque([[w, v, set([w])] for w, v in weight2value.items() if w <= K])

max_values = set([])
visit = []
while queue:
    weight, value, passed = queue.popleft()
    
    if passed not in visit:
        visit.append(passed)
        for w in list(weights-passed):
            if weight + w > K:
                max_values.add(value)
            else:
                temp_passed = passed.copy()
                temp_passed.add(w)
                queue.append([weight+w, value+weight2value[w], temp_passed])

print(max(max_values))