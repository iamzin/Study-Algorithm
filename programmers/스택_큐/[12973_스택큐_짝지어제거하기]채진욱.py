s = "ccaade"


def solution(s):
    num_st = []

    for i in s:
        if len(num_st) == 0:
            num_st.append(i)
        elif num_st[-1] == i:
            num_st.pop()
        elif num_st[-1] != i:
            num_st.append(i)

    print(num_st)

    if len(num_st) == 0:
        return 1
    else:
        return 0


print(solution(s))
