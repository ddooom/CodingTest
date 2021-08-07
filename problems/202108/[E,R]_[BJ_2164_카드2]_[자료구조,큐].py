# BJ 2164 카드2 <자료 구조, 큐>
# https://www.acmicpc.net/problem/2164
# 시간 : 15
# 문제 리뷰 : E, R
# 회고 : 해당 알고리즘을 그대로 구현하여 답에 규칙성을 파악한 뒤 pythonic하게 구현
#        Best Solution을 이를 :=와 int(,2)를 이용하여 효율적으로 구현하였다.


n = int(input())
print(n if n%2**(len(bin(n))-3)==0 else 2*n%2**(len(bin(n))-2))


''' Best Solution
print(int(bin(int(i:=input())*2)[3:],2)or i)
'''