# 연습문제 > 콜라츠 추측
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    count = 0
    while num > 1:
        if count == 500:
            return -1
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        count += 1
    return count

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(6))    # 8
print(solution(16))    # 4
print(solution(626331))    # -1

# 문제 풀이 시간: 3분

''' 더 좋은 코드
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1
'''
