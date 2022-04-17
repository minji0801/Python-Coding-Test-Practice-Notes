# a, b = 7, 34
a, b = map(int, input().split())
count = 0

# 두 수 차이의 절댓값이 0이될 때까지 수행
c = abs(a-b)
while c > 0:
  # -1, -5, -10을 한 결과의 절댓값이 제일 작으면 채택
  sub = [abs(c-1), abs(c-5), abs(c-10)]
  c = min(sub)
  count += 1

print(count)

# 문제 풀이 시간: 25분
