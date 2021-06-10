def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while len(progresses) > 0:
        if(progresses[0] + speeds[0] * time >= 100): # 진도율 100%가 넘을 경우
            progresses.pop(0) # 확인한 진도, 속도 제거
            speeds.pop(0)
            count += 1 # 카운팅
        else:
            if count > 0: # 진도율 100% 안 넘을 경우
                answer.append(count)
                count = 0
            time += 1 # 작업 일수 늘리기
            
    
    answer.append(count)
    return answer