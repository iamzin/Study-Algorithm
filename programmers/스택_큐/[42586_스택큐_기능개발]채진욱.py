import math

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

# 기능개발


def solution(progresses, speeds):
    answer = []

    for i in range(len(progresses)):
        # 작업 일수 [5, 10, 1, 1, 20, 1]
        progresses[i] = math.ceil((100-progresses[i])/speeds[i])

    front = 0  # 기준점

    for i in range(len(progresses)):
        if progresses[front] < progresses[i]:  # front보다 i가 큰 경우에는 기능 배포
            answer.append(i-front)  # 배포되는 기능 개수는 i-front
            front = i  # 기준점을 i로 바꿔줌

    answer.append(len(progresses)-front)  # 마지막에는 전체 개수에서 마지막 기준점 index를 뺴면 됨

    return answer


print(solution(progresses, speeds))