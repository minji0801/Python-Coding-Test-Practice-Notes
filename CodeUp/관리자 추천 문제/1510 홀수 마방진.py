# 링크: https://codeup.kr/problem.php?id=1510

# 마방진: 가로 세로 대각선의 합이 같은 사각형
'''
구현 방법:
1. 시작은 첫 행, 한 가운데 열에 1을 둔다.
2. 행을 감소, 열을 증가하면서 순차적으로 수를 넣어간다.
3. 행은 감소하므로 첫 행보다 작아지는 경우에는 마지막 행으로 넘어간다.
4. 열은 증가하므로 마지막 열보다 커지는 경우에는 첫 열로 넘어간다.
5. 넣은 수가 n의 배수이면 행만 증가한다. 열은 변화없음.
'''
# n = 3

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
x, y, z = 0, n//2, 1

for _ in range(n*n):
    board[x][y] = str(z)
    if z % n == 0:
        x += 1
    else:
        x -= 1
        if x < 0: x += n
        y += 1
        if y == n: y -= n
    z += 1

for i in range(n):
    print(' '.join(board[i]))

# 문제 풀이 시간: 25분
