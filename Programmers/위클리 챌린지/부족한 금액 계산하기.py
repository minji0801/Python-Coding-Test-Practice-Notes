# 위클리 챌린지 > 부족한 금액 계산하기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/82612?language=python3

# price: 원래 이용료, money: 처음 가지고 있던 금액, count: 이용 횟수
def solution(price, money, count):
    answer = (count * (price + (price * count))) // 2 - money
    return 0 if answer < 0 else answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(3, 20, 4))    # 10

# 문제 풀이 시간 : 10분

''' 더 좋은 코드
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
'''
