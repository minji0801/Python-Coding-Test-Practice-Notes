# 링크: https://codeup.kr/problem.php?id=2007

# n = 5
# data = [2, 5, 8, 10, 29]

n = int(input())
data = list(map(int, input().split()))

if sorted(data) == data:
    print("오름차순")
elif sorted(data, reverse=True) == data:
    print("내림차순")
else:
    print("섞임")

# 문제 풀이 시간: 5분
