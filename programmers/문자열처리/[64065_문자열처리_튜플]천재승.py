

def solution(s):
    answer = []

    s=s[2:-2]
    set_list=s.split('},{')
    set_list.sort(key=lambda x:len(x))
    for sl in set_list: 
        sl= sl.split(',')
        for s in sl:
            if s not in answer: 
                answer.append(s)
    answer=list(map(int, answer))

    return answer


solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")