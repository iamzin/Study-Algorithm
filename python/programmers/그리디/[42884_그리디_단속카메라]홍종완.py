# 단속 카메라 - 그리디 - 42884

# 고속도로를 이동하는 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한 번은 만나도록 카메라를 설치하려고 합니다.
# 고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때,
# 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.

def solution(routes):
    answer = 0
    routes.sort(reverse=True)
    # routes.sort()
    # routes.reverse()
    # 두번 째 원소 기준으로 정렬하기 -> 람다식 사용
    # routes.sort(key=lambda x: x[1])

    # print(routes)
    # 가장 큰 값으로 초기화
    temp = 30001
    for i in range(len(routes)):
        if temp > routes[i][1]:
            temp = routes[i][0]
            answer += 1

    return answer


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
