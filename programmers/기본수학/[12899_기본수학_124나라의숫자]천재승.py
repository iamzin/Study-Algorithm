# 12936_줄서는방법 과 유사한 문제였다.
# 내 풀이는 다른 풀이에 비해 너무 길다

def solution(n):
    answer = ''
    numbers='124'
    #자리수
    cnt=1
    #0번째를 고려해주기 위해서 1을 감소
    n-=1
    #자리수를 구한다.
    while 1:
        if n-3**cnt>=0: 
            n-=3**cnt
            cnt+=1
        else:
            break
            
    while cnt>0:
        #맨 앞자리 고정했을 때 나올 수 있는 경우의 수
        tmp=3**(cnt-1)
        #맨 앞자리 수가 위치한 idx
        idx=n//tmp
        #고정한 앞자리 수 제외한 나머지
        n=n%tmp
        #남은 자리 수
        cnt-=1
        
        answer+=numbers[idx]

    print(answer)
    return answer


solution(4)