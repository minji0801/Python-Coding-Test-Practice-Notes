# 쿠폰을 N개 모으면 아메리카노 한잔이랑 바꿀 수 있는데, 쿠폰 교환할 때도 쿠폰을 한 장 준다.

# k, n = 10, 3

k, n = map(int, input().split())
res = 0

# 아메리카노로 교환할 수 있을 때까지 반복
while k >= n:
    k -= n-1
    res += 1

print(res)

# 문제 풀이 시간: 7분
