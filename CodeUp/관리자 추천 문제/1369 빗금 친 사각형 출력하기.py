# 링크: https://codeup.kr/problem.php?id=1369

# n, k = 4, 1

n, k = map(int, input().split())

for i in range(0, n):
    # 왼쪽 아래로 빗금치기 위한 인덱스 번호
    j = k-1 if i % k == 0 else j-1

    # 모든 문자를 공백으로 초기화
    star = [' '] * n    
    
    # *로 빗금 처리
    z = 0
    while j+(k*z) < n-1:
        star[j+(k*z)] = '*'
        z += 1

    # 첫 번째와 마지막 줄은 모두 *, 이외에는 맨 앞과 끝을 *로 채우기
    if i == 0 or i == n-1:
        star = ['*'] * n
    else:
        star[0] = '*'
        star[-1] = '*'
        
    print(''.join(star))

# 문제 풀이 시간: 54분
