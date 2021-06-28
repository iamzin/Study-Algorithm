#시간복잡도: nlogn
def solution(routes):
    answer=0
    leng=len(routes)
    checked=[0]*leng
    camara= -30001
    #진출 기준 오름차순 정렬
    routes.sort(key= lambda x: x[1])
    #정렬 후, 임의 차량의 진출 지점(routes[i][1])이 뒤에 있는 차량의 
    #진입 지점(routes[j][0]보다 작으면 이동 경로가 겹치는 부분이 없음을 의미한다.
    for route in routes:
        #카메라가 차량 진입 지점보다 작은지 확인한다.
        #작다면, 현재 카메라 위치로 해당 차량을 만나지 못했다는 의미이니
        #카메라를 추가로 세우고, 가장 최근 카메라 위치를 갱신한다.
        if camara < route[0] :
            camara=route[1]
            answer+=1
            
    return answer

print(solution([[-20,0], [1,2], [3,4], [5,6]]))