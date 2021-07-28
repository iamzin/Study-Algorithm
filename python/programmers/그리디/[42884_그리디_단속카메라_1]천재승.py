#시간복잡도: n^2
def solution(routes):
    answer=0
    leng=len(routes)
    checked=[0]*leng

    #진출 기준 오름차순 정렬
    routes.sort(key= lambda x: x[1])
    #정렬 후, 임의 차량의 진출 지점(routes[i][1])이 뒤에 있는 차량의 
    #진입 지점(routes[j][0]보다 작으면 이동 경로가 겹치는 부분이 없음을 의미한다.
    for i in range(leng):
        if checked[i]==0:
            camara= routes[i][1]
            answer+=1
        for j in range(i+1, leng): 
            if routes[j][0]<= camara<=routes[j][1] and checked[j]==0:
                checked[j]=1

    return answer

print(solution([[-20,0], [1,2], [3,4], [5,6]]))