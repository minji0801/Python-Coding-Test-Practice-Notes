# 링크: https://codeup.kr/problem.php?id=1166

# year = 2012

'''
1. 해(year)가 4의 배수이면서 100의 배수가 아니면 윤년.
2. 400의 배수이면 윤년.
위 두 조건 중 하나라도 맞으면 윤년이다.
'''
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('yes')
else: 
    print('no')

# 문제 풀이 시간: 4분
