s = " people unFollowed     me daww12SS "

print(s[:-1])


def solution(s):  # 테스트케이스 8번만 안됨
    answer = ''
    word_list = s.split(" ")
    # print(word_list)
    for i in word_list:
        i = i.capitalize() + " "
        answer += i
    # answer = answer.rstrip() # 이 부분 대신 answer[:-1] 리턴하면 통과
    return answer[:-1]


def solution2(s):
    # word_list = [word.capitalize() for word in s.split(" ")]
    # answer = " ".join(word_list)
    return ' '.join([word.capitalize() for word in s.split(" ")])


print("|" + solution(s) + "|")
print("|" + solution2(s) + "|")
