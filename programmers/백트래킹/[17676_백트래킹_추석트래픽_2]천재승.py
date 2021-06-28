#출처: https://softworking.tistory.com/379
#처리시간: nlogn <-sort

def solution(lines):
    START=0
    END=1
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
        
        #각 작업을 1초 간 처리할 때, (처리 가능한 시작시간)의 시작과 끝 저장
        times.append((startMs-1000+1,START))
        times.append((endMs,END))
        
    #시간 순/ START->END 순으로 오름차순 정렬
    times.sort()

    #처리량
    throughput=0
    #동시간대 총 처리량 
    for time in times:
        if time[1]==START: 
            throughput+=1
        else: 
            throughput-=1

        # print(throughput)
        answer=max(answer,throughput)

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