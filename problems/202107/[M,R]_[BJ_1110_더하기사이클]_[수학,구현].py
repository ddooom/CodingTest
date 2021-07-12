# BJ 1110 더하기 사이클 <수학, 구현>
# https://www.acmicpc.net/problem/1110
# 시간 : 20
# 문제 리뷰 : M, R
# 회고 : 수의 자릿 수를 이용한 문제에서는 문자열로 해서 index를 사용하는 것보다 나머지와 몫으로 자릿수를 구하는 것이 더 빠르다.  
#        특정 값이 반복문에서 교체되어가며 변하는 것은 아래처럼 교체되는 값을 -1로 초기화하며 하는 것이 더 빠르다.
#        간단한 경우 함수를 사용하지 않는 것이 더 빠르다.


num = int(input())
new_num = -1
answer = 0
while num != new_num:
    if new_num == -1: new_num = num
    new_num = new_num%10*10 + (new_num//10 + new_num%10)%10 
    answer += 1

print(answer)