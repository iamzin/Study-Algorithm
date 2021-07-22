#전형적인 크루스칼 알고리즘 문제였다. 크루스칼 알고리즘은 가장 적은 비용으로 모든 노드를 연결하기 위해 사용하는 알고리즘이다. 다시 말해 최소 신장 트리를 만들기 위한 알고리즘이다.
#find와 union을 통해 부모노드를 찾고 연결시킨다. 부모노드가 서로 같으면 사이클이 생성되므로 union하지 않는다. 

def solution(n, costs):
    answer = 0

    #parent set
    parent=[k for k in range(n)]
    print(parent)
    #costs sort
    costs.sort(key=lambda x: x[2])

    #find 메소드
    def find(v): 
        if parent[v]==v: 
            return v
        parent[v]=find(parent[v])
        return parent[v]
      
            
    #union 메소드
    def union(v1,v2): 
        parent[find(v2)]=parent[find(v1)]

    for cost in costs:
        #부모가 같으면 사이클 생성을 의미하므로, 부모가 다르면 union해서 parent을 갱신한다(노드 간 연결을 의미한다).
        if find(cost[0])!= find(cost[1]): 
            union(cost[0], cost[1])
            answer+=cost[2]


    
    print(answer)
    return answer

solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])