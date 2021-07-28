clothes = [["yellowhat", "headgear"], [
    "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    
def solution(clothes):
    answer = 1
    col_dict = {}  # key(종류) - value(개수)

    for i in range(len(clothes)):
        if col_dict.get(clothes[i][1]):
            col_dict[clothes[i][1]] += 1
        else:
            col_dict[clothes[i][1]] = 1

    for i in col_dict:
        answer *= (col_dict[i]+1)  # 종류를 사용안하는 경우 +1

    answer -= 1  # 종류 전체 사용안하는 경우 -1

    return answer


print(solution(clothes))