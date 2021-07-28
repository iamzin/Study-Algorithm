#처리량 구하기
def getThroughput(times,start, end):
    cnt=0

    for time in times: 
        if start>time[1] or end<time[0]:
            continue
    
        cnt+=1
    return cnt

#처리시간:n^2
def solution(lines):
    times=[]
    answer = 0
    #line 마다 처리 시작/끝시간 구하기
    for line in lines:

        _, end, during=line.split(' ')
        hh, mm, ss=end.split(':')
        duringMs= float(during[:-1])*1000

        #시작/끝시간 s->ms 단위 변환
        endMs=(int(hh)*60*60+int(mm)*60+float(ss))*1000
        startMs=endMs-duringMs+1
        #시작/끝시간 저장
        times.append((startMs,endMs))

    #처리시간:n^2
    for time in times:
        #시작/끝시간 기준 처리량 비교
        answer= max(
            answer,
            getThroughput(times,time[0],time[0]+1000-1),
            getThroughput(times,time[1],time[1]+1000-1)
            )
        
    return answer


print(solution( [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))