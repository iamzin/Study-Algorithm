# 영어 끝말잇기 - 반복문 - 12981
# 1부터 n까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기를 하고 있습니다. 영어 끝말잇기는 다음과 같은 규칙으로 진행됩니다.

# 1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
# 마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
# 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
# 이전에 등장했던 단어는 사용할 수 없습니다.
# 한 글자인 단어는 인정되지 않습니다.

# 사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때,
# 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 하도록 solution 함수를 완성해주세요.

def solution(n, words):
    temp = []
    temp.append(words[0])
    prev_word = words[0]

    for i in range(1, len(words)):
        # 다음 단어의 첫글자와 이전 단어의 마지막글자가 다를 경우
        if words[i][0] != prev_word[-1]:
            return [i % n+1, i // n+1]
            # 인덱스 % 사람수 + 1, 인덱스 / 사람수의 몫 + 1
        # 이미 나온 단어일경우
        elif words[i] in temp:
            return [i % n+1, i // n+1]
        # 위 조건이 아닐시 변수 변경
        prev_word = words[i]
        # 위 조건이 아닐시 저장
        temp.append(words[i])

    return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel",
      "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage",
      "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))

# def solution(n, words):
#     answer = []
#     temp = set(words[0])

#     for w1, w2 in zip(words, words[1:]):
#         # 앞 뒤 끝말잇기 실패일 경우
#         if w1[-1] != w2[0]:
#             answer.append(words.index(w1) % n)
#             answer.append(words.index(w2)//n+1)
#             return answer
#         if w2 in temp:
#             answer.append(words[words.index(w2):].index(w1) % n+2)
#             answer.append(words[words.index(w2):].index(w1) // n+1)
#             return answer
#         temp.add(w1)

#     return [0, 0]
