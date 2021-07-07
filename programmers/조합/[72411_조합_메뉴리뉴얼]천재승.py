from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []


    for cnt in course:
        temp=[]
        for order in orders: 
            #정렬하지 않으면 같은 조합이라도 순서가 다르면 결과는 다르다.
            #combinations([A,B],2)와 combinations([B,A],2)는 다르다.
            #sorted를 사용해야 한다. sort는 list만 가능하다.
            order=sorted(order)
            combi=combinations(order,cnt)
            temp+=combi

        print(temp)
        
        # Coutner 중복된 원소 개수 셀 때 편리하다!
        # 딕셔너리 객체와 유사하다. 유니크한 원소의 이름들은 딕셔너리 key로, 
        # 각 원소의 카운트는 딕셔너리의 value로 저장된다.
        # Counter하면 type도 Counter이다! 
        counter= Counter(temp)
        #cnt로 만들 수 없거나 만들 수 있어도 개수가 1개인 조합은 제외
        if len(counter)!=0 and max(counter.values())!=1:
            #k는 튜플이므로 조인을 이용해서 str만들어준다.
            answer+=[ ''.join(k) for k in counter if counter[k]==max(counter.values()) ]


            
    return sorted(answer)


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])
    