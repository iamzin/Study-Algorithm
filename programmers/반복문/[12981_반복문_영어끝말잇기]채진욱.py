# 구하고자 하는 것
# "가장 먼저 탈락하는 사람의 번호"와 "그 사람이 자신의 몇 번째 차례에 탈락하는지"

# 탈락 조건
# - 이전에 나온 단어를 말하는 경우
# - 이전 단어 마지막 글자로 시작하는 단어를 말하지 않은 경우

# 탈락자 없는 경우
# - return [0,0]

import math

n = 3
words = ["tank", "kick", "know", "wheel",
         "land", "dream", "mother", "robot", "tank"]


def solution(n, words):  # 내 풀이

    answer = []
    word_list = []  # 끝말잇기에 사용되는 단어 리스트
    # ["가장 먼저 탈락하는 사람의 번호", "그 사람이 자신의 몇 번째 차례에 탈락하는지"]

    for i in range(0, len(words)-1):
        if words[i] in word_list:  # 현재 단어가 word_list에 있다면 탈락 조건
            # i가 0부터 시작이므로 실제 번호를 구하기 위해서는 i+1로 바꿔야함
            if (i+1) % n == 0:  # 탈락자 번호가 n인 경우
                answer.append(n)
            else:  # 탈락자 번호가 n이 아닌 경우
                answer.append((i+1) % n)  # 나머지를 통해 탈락자 번호를 구할 수 있음

            answer.append(math.ceil((i+1)/n))  # 탈락자의 몇번째 차례에 탈락하는지 구하는 부분
            return answer
        else:
            word_list.append(words[i])
            word_last = words[i][-1]  # 현재 단어의 마지막 글자
            next_word_first = words[i+1][0]  # 다음 단어의 첫번째 글자
            if word_last is not next_word_first:  # 현재 단어 마지막 글자랑 다음 단어 첫번째 글자가 다른 경우
                if (i+2) % n == 0:  # 실제 탈락자는 그 다음 단어를 말하는 사람이므로 i+2로 계산함
                    answer.append(n)
                else:
                    answer.append((i+2) % n)
                answer.append(math.ceil((i+2)/n))
                return answer

    if words[-1] in word_list:  # 위의 for문에서 words의 마지막 단어를 고려하지 않았으므로 words[-1]이 탈락자 조건 만족하는지 확인
        if len(words) % n == 0:
            answer.append(n)
        else:
            answer.append(len(word_list) % n)
        answer.append(math.ceil(len(word_list)/n))

    if len(answer) == 0:  # answer 아무 값도 없으면 탈락자가 없는 조건
        answer.append(0)
        answer.append(0)

    return answer


def solution2(n, words):
    # 처음 말한 단어 저장
    wordset = set([words[0]])

    # 이전 단어 기억
    prev_words = words[0]

    for i in range(1, len(words)):
        # 이전 단어의 마지막 글자와 제시단어의 첫 글자가 다르거나,
        # 이미 있는 단어일 경우
        if (prev_words[-1] != words[i][0] or words[i] in wordset):
            return [(i % n)+1, (i//n)+1]
        # 등장한 단어 저장
        wordset.add(words[i])
        # 제시단어 기억
        prev_words = words[i]
    return [0, 0]


def solution3(n, words):
    for p in range(1, len(words)):
        # words[:p] => words[0]부터 words[p-1]까지
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]:
            return [(p % n)+1, (p//n)+1]
    else:
        return [0, 0]

# print(solution(n, words))
