def solution(brown, yellow):
    answer = []
    multiply = brown + yellow

    for b in range(1, multiply+1):
        if (multiply / b) % 1 == 0:             # multiply == ab == brown + yellow
            a = multiply / b

            if a >= b:                          # a >= b 만족하는 경우가 되면,
                if 2*a + 2*b == brown + 4:      # 2*a + 2*b == brown + 4 조건 만족하는지 확인
                    return [a, b]               # 만족한다면 return

    return answer