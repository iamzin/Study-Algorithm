def solution(n):
    answer = 0
    # 이진수로 변환해서 1의 개수를 알아내야됨
    n_binary = changeToBinary(n)
    cnt = 0

    for i in n_binary:
        if i == 1:
            cnt += 1  # 1의 개수

    for i in range(n+1, 1000001):
        if changeToBinary(i).count(1) == cnt:
            answer = i
            break

    return answer


def changeToBinary(n):
    backward_b_list = []
    right_b_list = []

    while True:
        remain = n % 2
        backward_b_list.append(remain)
        n = n//2
        if n == 0 or n == 1:
            backward_b_list.append(n)
            break

    right_b_list = [0]*len(backward_b_list)

    for i in range(len(backward_b_list)-1, -1, -1):
        right_b_list[len(backward_b_list)-1-i] = backward_b_list[i]

    return right_b_list


print(solution(78))