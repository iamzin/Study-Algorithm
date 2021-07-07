def solution(people, limit):
    answer = 0
    
    left=0 
    right= len(people)-1
    #보트의 개수를 최소로 하려면, 최소 무게와 최대 무게를 합(보트는 최대 2명)이 무게제한을 통과해야 한다.
    people.sort()
    while left<=right:
        #최소, 최대 무게 합이 무게제한을 통과할 경우
        if people[left]+people[right]<=limit:
            left+=1

        #무게제한을 통과하든 안하든 최대 무게 1명은 보트를 태워야 한다.    
        right-=1
            
        answer+=1
    return answer