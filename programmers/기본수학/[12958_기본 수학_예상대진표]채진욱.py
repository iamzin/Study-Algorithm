def solution(n, a, b):  # 내 풀이
    answer = 0
    round = 1

    print("n,a,b: ", n, a, b)

    while n != 2:  # 최종 라운드 전까지

        if a-b == 1 and a % 2 == 0:  # a가 클 경우: a와 b가 같은 경기를 치루는지 확인
            print("n,a,b: ", n, a, b)
            return round

        if b-a == 1 and b % 2 == 0:  # b가 클 경우: a와 b가 같은 경기를 치루는지 확인
            print("n,a,b: ", n, a, b)
            return round

        # 다음 라운드의 a와 b의 번호 계산
        if a % 2 != 0:
            a = a//2 + 1
        else:
            a = a//2

        if b % 2 != 0:
            b = b//2 + 1
        else:
            b = b//2

        # 다음 라운드의 n 과 round 계산
        n = n//2
        round += 1

        print("n,a,b: ", n, a, b)

    return round


def solution2(n, a, b):  # 참고한 풀이
    answer = 0

    while a != b:
        answer += 1  # 라운드+1
        a, b = (a+1)//2, (b+1)//2  # 홀수 짝수 상관없이 2로 나눈 몫은 같기때문에 가능

    return answer


print(solution2(8, 2, 3))
