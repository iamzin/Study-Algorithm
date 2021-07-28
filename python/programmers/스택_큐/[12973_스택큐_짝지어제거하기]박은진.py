def solution(s):
    stack = []
    for x in s:
        if not stack:
            stack.append(x)
        else:
            if stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)

    if stack:
        return 0
    else:
        return 1


# 종완님
# 초기에 홀수인 경우 바로 return 0 하도록 조건문 추가