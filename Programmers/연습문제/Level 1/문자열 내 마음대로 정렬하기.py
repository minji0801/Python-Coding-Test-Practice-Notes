# 연습문제 > 문자열 내 마음대로 정렬하기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3

# 각 단어의 n 번째 문자를 기준으로 오름차순 정렬
def solution(strings, n):
    return sorted(sorted(strings), key = lambda x: x[n])

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(["sun", "bed", "car"], 1))    # ["car", "bed", "sun"]
print(solution(["abce", "abcd", "cdx"], 2))    # ["abcd", "abce", "cdx"])

# 문제 풀이 시간: 23분
