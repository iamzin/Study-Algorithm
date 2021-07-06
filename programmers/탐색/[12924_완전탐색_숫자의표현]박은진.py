def solution(n):
    c = 0

    for i in range(1, n):
        s = i
        
        for j in range(i+1, n):
            s += j
            
            if s == n:
                c += 1
                break
            elif s > n:
                break
    
    return c+1