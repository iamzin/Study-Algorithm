# 디스크 컨트롤러 - 힙 - 42627
# 하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다.
# 가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.

# 각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때,
# 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요.
# (단, 소수점 이하의 수는 버립니다)
import heapq


def solution(jobs):
    answer = 0
    before = -1
    after = 0
    count = 0
    task = []

    while count < len(jobs):
        for job in jobs:
            # 앞에 진행되고 있는 작업중에 작업 요청을 받았더라면 해당 task끝나기 전까지 사이의 시간 추가
            if before < job[0] <= after:
                answer += (after-job[0])
                # 중간에 작업 요청을 받았기 때문에 task에 추가시켜준다
                heapq.heappush(task, job[1])

        # task가 존재할때
        if task:
            # 다른 작업이 진행중이라 작업을 진행하지 못하지만 요청이 들어왔기 때문에 시간은 추가해준다
            answer += task[0]*len(task)

            # 시간 time변경
            before = after
            after += heapq.heappop(task)

            # 하나의 task가 끝났기 때문에 count를 추가시켜준다
            count += 1

        # task가 없을때
        else:
            # 시간만 흐르게 냅둔다
            after += 1

    return int(answer/len(jobs))


print(solution([[0, 3], [1, 9], [2, 6]]))
