"""문제
회전판에 먹어야 할 N 개의 음식이 있다.
각 음식에는 1부터 N 까지 번호가 붙어있으며, 각 음식을 섭취하는데 일정 시간이 소요된다.
무지는 다음과 같은 방법으로 음식을 섭취한다.

무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓는다.
마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 온다.
무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취한다.
다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식을 말한다.
회전판이 다음 음식을 무지 앞으로 가져오는데 걸리는 시간은 없다고 가정한다.
무지가 먹방을 시작한 지 K 초 후에 네트워크 장애로 인해 방송이 잠시 중단되었다.
무지는 네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야 하는지를 알고자 한다.
각 음식을 모두 먹는데 필요한 시간이 담겨있는 배열 food_times, 네트워크 장애가 발생한 시간 K 초가 매개변수로 주어질 때 몇 번 음식부터 다시 섭취하면 되는지 return 하도록 solution 함수를 완성하라.
"""
import heapq

def solution(food_times, k):
    if sum(food_times)<=k:
        return -1
    # 시간이 작은 음식부터 빼야 하니까 우선순위 큐 적용
    q = []
    for i in range(len(food_times)):
        # (음식시간, 음식번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q,(food_times[i],i+1))
        
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간
    
    length = len(food_times)  # 남은 음식의 개수
    while sum_value + ((q[0][0]-previous)*length)<k:
        now = heapq.heappop(q)[0]
        sum_value += (now+previous) * length
        length -= 1
        previous = now
    result = sorted(q,key=lambda x:x[1])
    return result[(k-sum_value)%length][1]

print(solution([3, 1, 2], 5)) # 답 :1
