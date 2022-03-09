# 연습문제 > 제일 작은 수 제거하기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3

def solution(arr):
    arr.remove(min(arr))
    return [-1] if not arr else arr

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([4, 3, 2, 1]))    # [4, 3, 2]
print(solution([10]))    # [-1]

# 문제 풀이 시간: 3분
