def check_distance(place):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    for x in range(5):
        for y in range(5):
            z = place[x][y]
            if z == 'X': continue

            # 상하좌우에 'P' 개수 세기
            count_P = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5:
                    if place[nx][ny] == 'P':
                        count_P += 1

            # 'P'를 기준으로 상하좌우에 'P'가 한 명이라도 있으면 거리두기 지키지 않음
            # 'O'를 기준으로 상하좌우에 'P'가 두 명이상이면 거리두기 지키지 않음
            if (z == 'P' and count_P > 0) or (z == 'O' and count_P > 1): 
                return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        place = [list(p) for p in place]
        answer.append(check_distance(place))
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))    # [1, 0, 1, 1, 1]

'''
POOOP | POOPX
OXXOX | OXPXP
OPXPX | PXXXO
OOXOX | OXXXO
POXXP | OOOPP
'''

# 문제 풀이 시간: 46분
