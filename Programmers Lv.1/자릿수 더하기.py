# 연습문제 > 자릿수 더하기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12931?language=python3

def solution(n):
    return sum(list(map(int, list(str(n)))))
    
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(123))    # 6
print(solution(987))    # 24

# 문제 풀이 시간: 3분

''' 더 좋은 코드
def sum_digit(number):
    return sum(map(int,str(number)))
'''
