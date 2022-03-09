# 연습문제 > 자연수 뒤집어 배열로 만들기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12932?language=python3

def solution(n):
    return list(map(int, reversed(list(str(n)))))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(12345))    # [5, 4, 3, 2, 1]

# 문제 풀이 시간: 3분

''' 더 좋은 코드
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
'''
