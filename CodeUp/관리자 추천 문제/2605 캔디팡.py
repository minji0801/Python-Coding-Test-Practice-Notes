# 링크: https://codeup.kr/problem.php?id=2605
# 7 * 7 모양의 격자 판에 같은 색깔이 연속 3개 이상인 부분이 터짐

board = []
for _ in range(7):
    board.append(list(map(int, input().split())))

from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]    # 상하좌우

def bfs(x, y, board, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True    # 방문 처리

    color = board[x][y]    # 현재 칸의 색상
    count = 1    # 같은 색의 칸 개수

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 칸에서 상하좌우 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 보드 넘어서면 무시하기
            if nx < 0 or nx >= 7 or ny < 0 or ny >= 7:
                continue

            # 칸의 색상이 동일하고 방문한 적 없으면 재귀 (그 칸을 기준으로 다시 상하좌우 확인)
            if board[nx][ny] == color and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True    # 방문처리
                count += 1

    # 색상이 같은 부분이 3개 이상이면
    if count >= 3:
        return True
    else:
        return False

visited = [[False for _ in range(7) ] for _ in range(7)]    # 방문 여부
res = 0    # 터지는 영역의 개수

for i in range(7):
    for j in range(7):
        if not visited[i][j]:
            if bfs(i, j, board, visited):
                res += 1

print(res)

# 문제 풀이 시간: 45분
