#다른 사람의 풀이
def solution(n, words):
    for i in range(1,len(words)):
        if words[i][0]!=words[i-1][-1] or len(words[i])==1 or words[i] in words[:i]:
            return [(i%n)+1, (i//n)+1]

    return [0,0]

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))