# queue: FIFO, [2, 3, 5]의 형태

from collections import deque
def solution(prices):
    answer = []
    
    prices = deque(prices) # que로 캐스팅
    while prices:
        cnt = 0
        price = prices.popleft() # First Out
        
        for i in prices:
            cnt += 1 # 카운팅 
            if price > i: 
                break
                
        answer.append(cnt)
    return answer


# # [종완] 슬라이싱으로 처리: 효율성 실패 / 슬라이싱의 경우 객체들을 꺼내오는 과정이기 때문에 
# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         cnt = 0
#         for j in prices[i:]:
#             if prices[i] <= j:
#                 cnt += 1
#             else:
#                 cnt += 1
#                 break
#         answer.append(cnt-1)
#     return answer

# # [진욱] 범위 줄이기로 처리: 꺼내오는 과정 없이 본 배열에서 범위를 찍어주었기 때문에 효율성 통과
# def solution(prices):
#     answer = []

#     for i in range(len(prices)-1):
#         cnt = 0
#         for j in range(i+1, len(prices)):
#             if prices[i] <= prices[j]:
#                 cnt += 1
#             else:
#                 cnt += 1
#                 break
#         answer.append(cnt)

#     answer.append(0)

#     return answer