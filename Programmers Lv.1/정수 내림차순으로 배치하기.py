# 연습문제 > 정수 내림차순으로 배치하기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    nums = list(str(int(n)))
    return int(''.join(sorted(nums, reverse = True)))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(118372))    # 873211

# 문제 풀이 시간: 22분
