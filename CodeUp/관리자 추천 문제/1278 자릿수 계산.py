# 링크: https://codeup.kr/problem.php?id=1278

# n = 932

n = int(input())

count = 0
while n > 0:
    n = n // 10
    count += 1

print(count)

# 문제 풀이 시간: 3분
