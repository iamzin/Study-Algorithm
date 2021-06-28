def solution(s):
    answer = ''
    s.lower()

    s= s.split(' ')
    for i in range(len(s)) :
        s[i]= s[i].capitalize()

        if i<len(s)-1:
            answer+= s[i]+' '
        else: 
            answer+=s[i]


    return answer


print(solution("for the last week"))