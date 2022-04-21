# 전파가 닿지 않는 곳의 길이 구하기(L)
# trunc(L/(w*2+1)) + 1

from math import ceil
def solution(n, stations, w):
    answer = 0
    for i in range(len(stations)):
        station = stations[i]

        # 기지국 앞쪽 구간 확인
        if i == 0: prev = 0
        else:  prev = stations[i-1]+w

        # L: 전파가 도달하지 않는 구간의 길이
        L = (station-w)-prev-1    
        answer += ceil(L/(w*2+1))

        # 마지막 기지국은 뒷쪽 구간 확인
        if i == len(stations)-1:
            L = n-(station+w)
            answer += ceil(L/(w*2+1))

    return answer

print(solution(11,[4, 11],1))    # 3
print(solution(16,[9],2))    # 3
print(solution(11,[1, 11],1))    # 3
print(solution(11,[3, 11],1))    # 3

# 문제 풀이 시간: 57분

'''
def solution(n, stations, w):
    ans = 0
    idx = 0
    location = 1

    while(location <= n) :
        if(idx < len(stations) and location >= stations[idx]-w) :
            location = stations[idx]+w+1
            idx += 1
        else :
            location += 2*w+1
            ans += 1
    return ans
'''
