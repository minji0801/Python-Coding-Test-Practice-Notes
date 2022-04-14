# 링크: https://codeup.kr/problem.php?id=2008

n = int(input())
data = list(map(int, input().split()))

if len(set(data)) == 1:
    print("섞임")
elif sorted(data) == data:
    print("오름차순")
elif sorted(data, reverse=True) == data:
    print("내림차순")
else:
    print("섞임")

# 문제 풀이 시간: 4분
