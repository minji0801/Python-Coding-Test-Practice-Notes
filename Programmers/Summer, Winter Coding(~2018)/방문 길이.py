# Summer/Winter Coding(~2018) > 방문 길이
# 링크: https://programmers.co.kr/learn/courses/30/lessons/49994

# 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이
# 단, 좌표평면의 경계를 넘어가는 명령어는 무시합니다.

# 1. [[(start좌표),(end좌표)]]로 dirs 정리하기
# 2. x, y좌표의 절댓값이 5를 넘으면 무시하기
# 3. len(dirs)에서 겹치는 길의 개수 뺀 값 return

def solution(dirs):
    start, end = (0, 0), (0, 0)
    visited = []
    
    for dir in dirs:
        end = move(dir, start)
        
        if abs(end[0]) > 5 or abs(end[1]) > 5: continue
        if ([start, end] not in visited) and ([end, start] not in visited):
            visited.append([start, end])
        start = end

    return len(visited)

def move(command, start):
    if command == 'U':    # 위로 한 칸
        return (start[0], start[1]+1)
    elif command == 'D':    # 아래로 한 칸
        return (start[0], start[1]-1)
    elif command == 'R':    # 오른쪽으로 한 칸
        return (start[0]+1, start[1])
    elif command == 'L':    # 왼쪽으로 한 칸
        return (start[0]-1, start[1])
        
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("ULURRDLLU"))    # 7
print(solution("LULLLLLLU"))    # 7

# 문제 풀이 시간: 30분

''' 더 좋은 풀이
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2
'''
