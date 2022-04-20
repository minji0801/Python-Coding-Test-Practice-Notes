# 처음 걸어본 길의 길이

def solution(dirs):
    answer = 0
    x, y = 0, 0
    d = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    road = []

    for dir in dirs:
        nx, ny = x + d[dir][0], y + d[dir][1]

        # 이미 가본 길이면 pass
        if [(x,y,nx,ny)] in road or [(nx,ny,x,y)] in road:
            x, y = nx, ny
            continue

        # 범위 안에 있을 때만 처리
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            road.append([(x,y,nx,ny)])
            road.append([(nx,ny,x,y)])
            x, y = nx, ny
            answer += 1
        
    return answer

print(solution("ULURRDLLU"))    # 7
print(solution("LULLLLLLU"))    # 7

# 문제 풀이 시간: 17분
