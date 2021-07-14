# H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
# 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
# 입출력 예
# citations	return
# [3, 0, 6, 1, 5]	3

def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    print(citations)
    #[12,11,10] return 3
    #h의 후보 중 최대가 되는 수는 논문의 수(위의 예제: 3)이다.
    #위의 예제에서 h=3이 되려면 최소 앞에서 3번째 값이 3 이상이여야 한다. 
    #만약, [6,5,3,1,0]에서 h=5(h의 후보 중 최대수)이 되려면 앞에서 5번째 값이 5이상이여야 하는데 실제 값은 0이므로 h의 조건을 성립하지 않는다.
    #이런 식으로, h의 후보 중 최대수부터 1씩 감소시키면서 조건을 확인하면 H-Index을 구할 수 있다.
    for h in range(len(citations),0,-1): 
        min_num=citations[h-1]
        if min_num>=h:
            answer=h
            break
            
    return answer


solution([3, 0, 6, 1, 5])