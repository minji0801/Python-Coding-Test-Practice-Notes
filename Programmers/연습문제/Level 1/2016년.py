# 연습문제 > 2016년
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3

# 20160101 = FRI
# 2월은 29일까지
from datetime import date
def solution(a, b):
    week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return week[date(2016, a, b).weekday()]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(5, 24))    # "TUE"

# 문제 풀이 시간: 34분

''' 더 좋은 코드
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]
'''
