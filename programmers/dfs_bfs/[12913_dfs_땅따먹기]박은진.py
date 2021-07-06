# X : DP(동적계획법)

def solution(land):
    for i in range(len(land)-1):
        land[i+1][0] = max(land[i][1], land[i][2], land[i][3]) + land[i+1][0]
        land[i+1][1] = max(land[i][0], land[i][2], land[i][3]) + land[i+1][1]
        land[i+1][2] = max(land[i][0], land[i][1], land[i][3]) + land[i+1][2]
        land[i+1][3] = max(land[i][0], land[i][1], land[i][2]) + land[i+1][3]
    
    return max(land[-1])
    

# for i in range(1,len(land)):
#     for j in range(len(land[0])):
#         land[i][j] += max(land[i-1][:j] + land[i-1][j+1:]) # 기준 값 빼고 양 옆의 값들에 대해 max 비교

# return max(land[len(land)-1])