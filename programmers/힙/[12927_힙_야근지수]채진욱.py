import heapq

works = [1, 1, 1]
n = 9

# 매 시간 works 중 가장 큰 값을 -1
# 최대힙 사용해서 맨 앞에 있는 애를 계속 뽑아 씀 => heapq 라이브러리는 최소힙으로 구현되어있음
# works의 원소에 -1을 곱해서 최소힙을 구현


def solution(n, works):
    answer = 0
    minus_works = [i*(-1) for i in works]
    heapq.heapify(minus_works)
    print("minus_works: ", minus_works)

    while n != 0:
        recent_min = heapq.heappop(minus_works)
        if len(minus_works) == 0:  # heap의 원소가 다 pop되고 없는 경우
            break
        print("recent_min: ", recent_min)
        if recent_min < 0:
            recent_min += 1
            heapq.heappush(minus_works, recent_min)
            print("minus_works: ", minus_works)
        n -= 1

    for i in minus_works:
        answer += i ** 2

    return answer


print(solution(n, works))
