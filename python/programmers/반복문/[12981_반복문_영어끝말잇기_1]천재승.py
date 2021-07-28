def solution(n, words):
    word_list=[]
    for i in range(0,len(words)):
        # 번호
        number=i%n+1
        # 차례
        cnt=i//n+1
        # 탈락조건
        if len(words[i])==1 or (i>0 and words[i-1][-1]!=words[i][0]) or (words[i] in word_list): 
            return [number,cnt]
        # 새로운 단어가 나오면 리스트에 넣어준다.
        word_list.append(words[i])
    # print(word_list)
    return [0,0]

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))


