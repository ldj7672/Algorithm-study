"""
- 문제
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
- 입력
첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 
시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.
- 출력
첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.
"""

# n = 11
# s = [[1,4],[3,5],[0,6],[5,7],[3,8],[5,9],[6,10],[8,11],[8,12],[2,13],[12,14]]
n = int(input())
s = []
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])

s = sorted(s, key=lambda a: (a[1],a[0])) # 회의가 끝나는 시간 순으로 정렬하고, 끝나는 시간이 같은 경우에 시작 시간이 빠른 순으로 정렬

last = 0
cnt = 0
for i, j in s:
    if i >= last:   # 마지막 회의 끝난 시간보다 이번 회의 시작 시간이 더 느리면 회의 + 
        cnt += 1
        last = j    # 이번 회의 끝나는 시간을 마지막 회의 끝난 시간으로
print(cnt)
