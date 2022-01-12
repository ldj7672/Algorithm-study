"""문제
N개의 동전이 있을때(단위가 다 다름), N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하세요.
"""
"""해설
정렬을 이용한 그리디 알고리즘으로 푼다. 
화폐 단위를 기준으로 오름차순으로 정렬하고 1부터 차례대로 특정한 금액을 만들 수 있는지 확인.
"""
# n = int(input())
# data = list(map(int,input().split()))
n=5
data = [3,2,1,1,9] 
data.sort() # 1,1,2,3,9

target=1 # target : 만들 수 있는 금액인지?
for x in data:
  if target<x:
    break
  target +=x

print(target)