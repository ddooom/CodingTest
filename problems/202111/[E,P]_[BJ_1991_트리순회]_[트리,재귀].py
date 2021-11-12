# BJ 1991 트리 순회 <트리, 재귀>
# https://www.acmicpc.net/problem/1991
# 시간 : 10
# 문제 리뷰 : E, P
# 회고 : 


def forward_search(p):
    global forward
    child = tree[p]
    
    forward += p
    
    if child[0] != '.': 
        forward_search(child[0])
        
    if child[1] != '.': 
        forward_search(child[1])

def mid_search(p):
    global mid
    child = tree[p]
    
    if child[0] != '.': 
        mid_search(child[0])
    
    mid += p
    
    if child[1] != '.': 
        mid_search(child[1])

def backward_search(p):
    global backward
    child = tree[p]
    
    if child[0] != '.': 
        backward_search(child[0])
    
    if child[1] != '.': 
        backward_search(child[1])
        
    backward += p
        
tree = {}
for _ in range(int(input())):
    p, c1, c2 = input().split()
    tree[p] = [c1, c2]

forward = ''
mid = ''
backward = ''

forward_search('A')
mid_search('A')
backward_search('A')

print(forward)
print(mid)
print(backward)