from itertools import chain

def solution(n):
    answer=[]
    #삼각형 구조 만들기
    maps=[[0 for j in range(0,n)] for i in range(0,n)] 
    #초기 좌표
    row,col= -1,0
    #초기 번호
    num=1
    #방향 변경을 반복하면서 값이 증가
    #3방향으로 1번 씩 순회
    for i in range(0, n):
        for j in range(i,n):
            #방향을 알려주는 변수 생성
            if i%3==0: 
                row+=1
            elif i%3==1:
                col+=1

            else: # i%3==2
                row-=1
                col-=1

           
            maps[row][col]=num
            num+=1

    # answer = [ i for i in chain(*maps) if i!=0 ]

    for i in range(0,n): 
        for j in range(0,n):
            if maps[i][j]!=0:
                answer.append(maps[i][j])
    return answer

print(solution(4))