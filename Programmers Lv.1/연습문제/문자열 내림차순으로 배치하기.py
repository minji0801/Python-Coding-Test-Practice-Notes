# 연습문제 > 문자열 내림차순으로 배치하기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3

def solution(s):
    return ''.join(sorted(s, reverse = True))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("Zbcdefg"))    # "gfedcbZ"

# 문제 풀이 시간: 2분


