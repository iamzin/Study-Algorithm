# 코딩테스트 참여 개발언어 항목에 cpp, java, python 중 하나를 선택해야 합니다.
# 지원 직군 항목에 backend와 frontend 중 하나를 선택해야 합니다.
# 지원 경력구분 항목에 junior와 senior 중 하나를 선택해야 합니다.
# 선호하는 소울푸드로 chicken과 pizza 중 하나를 선택해야 합니다.
import bisect
def calc(table,a,b,c,d,e):
    idx= bisect.bisect_left(table[a][b][c][d], e)
    return len(table[a][b][c][d])-idx

def solution(info, query):
    language=["-", "cpp", "java", "python"]
    work=["-", "backend", "frontend"]
    career=["-", "junior", "senior"]
    food=["-", "chicken", "pizza"]

    answer = []
    table={}
    
    #init table
    for a in language: 
        table[a]={}
        for b in work: 
            table[a][b]={}
            for c in career:
                table[a][b][c]={}
                for d in food: 
                    table[a][b][c][d]=[]
                    
    
    #insert item into table
    for s in info: 
        a,b,c,d,e =s.split()

        for w in ["-",a]:
            for x in ["-",b]:
                for y in ["-",c]:
                    for z in ["-",d]:
                        table[w][x][y][z].append(int(e))

    #sort
    for a in language:
        for b in work:
            for c in career:
                for d in food:
                    table[a][b][c][d].sort()


    for q in query: 
        a,aa,b,bb,c,cc,d,e= q.split()

        answer.append(calc(table,a,b,c,d,int(e)))                   
        
    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
