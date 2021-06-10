def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while len(progresses) > 0:
        if(progresses[0] + speeds[0] * time >= 100): # 진도율 100%가 넘을 경우
            progresses.pop(0) # 확인한 진도, 속도 제거 [종완] deque를 활용해서 pop.left가 더 빠름, index를 따지는게 속도가 많이 느림
            speeds.pop(0)
            count += 1 # 카운팅
        else:
            if count > 0: # 진도율 100% 안 넘을 경우
                answer.append(count)
                count = 0
            time += 1 # 작업 일수 늘리기
            
    
    answer.append(count)
    return answer


# # [진욱] 작업일수 먼저 확인 후 처리: 
# def solution(progresses, speeds):
#     answer = []

#     for i in range(len(progresses)):
#         progresses[i] = math.ceil((100-progresses[i])/speeds[i])  # 작업 일수 [5, 10, 1, 1, 20, 1]

#     front = 0  # 기준점

#     for i in range(len(progresses)):
#         if progresses[front] < progresses[i]:  # front보다 i가 큰 경우에는 기능 배포
#             answer.append(i-front)  # 배포되는 기능 개수는 i-front
#             front = i  # 기준점을 i로 바꿔줌

#     answer.append(len(progresses)-front)  # 마지막에는 전체 개수에서 마지막 기준점 index를 뺴면 됨

#     return answer