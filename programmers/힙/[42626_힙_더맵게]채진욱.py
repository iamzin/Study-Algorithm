from collections import deque
import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7

# 최소 힙으로 두개 구해서 계산 하고
# 모든 값이 K 이상인지 확인
# K 이하가 있다면
# 다시 최소 힙으로 두개 구해서 계산하고
# 반복
# 값이 한개 밖에 없다면 return -1

# heap 자료구조 참고자료 https://littlefoxdiary.tistory.com/3


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # scoville 리스트를 즉각적으로 힙 자료형으로 변환
    while len(scoville) > 1:
        min_first = heapq.heappop(scoville)
        min_second = heapq.heappop(scoville)

        mixed = min_first + min_second*2
        heapq.heappush(scoville, mixed)

        answer += 1

        if scoville[0] >= K:
            return answer

    return -1


# solution(scoville, K)

# Queue를 활용한 풀이
# 코드들을 보니 다들 import heapq를 하셨는데 저는 heap을 몰라서..ㅎㅎ
# queue만 써서 풀었는데도 시간이 heap을 쓴 풀이의 절반 정도 걸리네요.
# 저는 섞어서 나온 새로운 값, mix들을 별도의 queue에 넣었는데 이게 가장 큰 요인같네요.
# 나중에 나온 mix값이 먼저 나온 것보다 클 수밖에 없어서 섞는 순서대로 queue에 넣어주면 크기 순서를 신경 쓸 필요가 없어요.
# 그냥 popleft로 꺼내면 무조건 mix값의 최소입니다ㅎ

def solution2(scoville, K):
    mixq = deque()
    scoville.sort()
    scovilleque = deque(scoville)

    while True:
        min_first = scovilleque.popleft()
        min_second = scovilleque.popleft()

        mixed = min_first + min_second*2
        mixq.append(mixed)
