#이분탐색
def count(table, idx, score): 
    list=table[idx]
    left=0
    right=len(list)-1
    result=0
    while left<=right:
        mid=(left+right)//2
        if list[mid]>=score:
            result=mid
            right=mid-1
        else: 
            left=mid+1
    
    return len(list)-result

def solution(info, query):
            
    answer = []
    wmap={'-':0, 'cpp':1, 'java': 2, 'python':3,
            'backend':1, 'frontend':2,
            'junior':1, 'senior':2,
            'chicken':1, 'pizza':2}
        
    #init table
    table=[[] for _ in range(4*3*3*3)]

    #insert item into table
    for string in info:
        a,b,c,d,e= string.split()
        # print(a,b,c,d,e)
        pos=(wmap[a]*3*3*3,wmap[b]*3*3, wmap[c]*3, wmap[d])
        score=int(e)

        for i in range(1<<4): 
            idx=0
            for j in range(4): 
                if i & (1<<j):
                    idx+=pos[3-j]
            table[idx].append(score)

    #sort
    for i in range(4*3*3*3): 
        table[i].sort()
            
    for string in query: 
        a,aa,b,bb,c,cc,d,e=string.split()
        idx=wmap[a]*3*3*3+wmap[b]*3*3+wmap[c]*3+wmap[d]
        score=int(e)
        answer.append(count(table, idx, score))
    
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))