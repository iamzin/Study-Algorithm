def solution(brown, yellow):
    answer = []
    sum=brown+yellow

    for h in range(3, sum+1,1):
        print(h)
        if sum%h==0:
            w=sum//h
            if (w-2)*(h-2)==yellow:
                answer.append(w)
                answer.append(h)
                break
        
    return answer

print(solution(24,24))