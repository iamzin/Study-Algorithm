from itertools import permutations

expression = "100-200*300-500+20"


# 리스트에 숫자, 수식으로 저장
# 가능한 수식 우선순위 -> permutation 사용
# 모든 경우에 대해 계산
# 계산은 stack 사용
# 계산 후 절대값화
# 가장 큰 수 찾기


def solution(expression):
    total_list = []  # 해당 expression을 리스트 화 해서 저장 # ['50', '*', '6', '-', '3', '*', '2']
    exp_list = set()  # expression에 있는 연산자를 중복 없이 set으로 저장 # {'*', '-'}
    stack = []  # 연산자 우선순위에 대한 계산을 할때 stack 사용
    sum_list = []  # 연산자 우선순위 별로 나오는 결과값을 저장하는 리스트

    num = ""  # expression을 total_list에 저장할 때 사용

    for i in range(len(expression)):
        if expression[i] == "*" or expression[i] == "-" or expression[i] == "+":
            total_list.append(num)
            exp_list.add(expression[i])
            num = ""
            total_list.append(expression[i])
        else:
            num += expression[i]
            if i == len(expression)-1:
                total_list.append(num)

    print("total_list: ", total_list)  # ['50', '*', '6', '-', '3', '*', '2']
    print("exp_list: ", exp_list)  # {'*', '-'}

    temp_list = total_list  # 여러가지의 연산자 우선순위를 계산하기 위해서는 total_list가 필요한데
    # 바로 total_list를 쓰게 되면 다음 연산자 우선순위를 계산하기 어렵기 때문에
    # 임시적인 temp_list에 total_list 값을 저장해서 사용

    # 입력된 연산자들로 가능한 우선순위 배열
    for permute in permutations(list(exp_list), len(exp_list)):
        for exp in permute:  # 현재 연산자 우선순위대로 연산자 계산
            for i in range(0, len(temp_list)):
                if i == 0:
                    stack.append(temp_list[i])
                    continue
                if stack[-1] == exp:  # stack 맨 위가 현재 연산자라면
                    recent_sik = stack.pop()  # stack 맨 위 pop하면 현재 연산자
                    prev_num = stack.pop()  # 다음으로 stack에서 pop 하면 이전 숫자
                    print("Stack: ", stack)
                    temp = eval(str(prev_num) + recent_sik +
                                str(temp_list[i]))  # 현재 연산자가 나온 식을 계산해서
                    print("temp: ", temp)
                    stack.append(temp)  # 스택에 저장
                else:  # stack 맨 위가 현재 연산자가 아니라면
                    stack.append(temp_list[i])
            print("stack: ", stack)
            # 연산자 우선순위 대로 계산하고 나온 나머지 식이 stack에 저장되어 있으므로 반복문을 도는 temp_list를 stack으로 바꿔줌
            temp_list = stack
            stack = []  # stack은 연산자 우선순위 대로 계산할때 마다 필요하므로 초기화
            print("temp_list: ", temp_list)
        # 현재 연산자 우선순위대로 나온 최종 결과값을 절대값 변환해서 sum_list에 저장
        sum_list.append(abs(temp_list[0]))
        temp_list = total_list  # 다음 연산자 우선순위를 계산하기 위해서 temp_list를 기존 식이 다 들어있는 total_list로 바꿔줌
    print("sum_list: ", sum_list)

    return max(sum_list)  # 최종적으로 sum_list에 있는 최대값을 반환


print(solution(expression))
