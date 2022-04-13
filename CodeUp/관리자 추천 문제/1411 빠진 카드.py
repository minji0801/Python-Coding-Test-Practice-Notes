# 링크: https://codeup.kr/problem.php?id=1411

# n = 10
# cards = [1, 2, 3, 4, 5, 6, 7, 9, 10]

n = int(input())
cards = [i for i in range(1, n+1)]

for _ in range(n-1): 
    cards.remove(int(input()))

print(cards[0])

# 문제 풀이 시간: 10분
