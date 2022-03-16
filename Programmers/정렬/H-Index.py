# 정렬 > H-Index
# 링크: https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = [0]
    count = 0
    for h in range(1, len(citations)+1):
        for n in citations:
            count += 1 if n >= h else 0
        if count >= h: answer.append(h)
        count = 0
    return max(answer)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([3, 0, 6, 1, 5]))    # 3
print(solution([0, 0, 0]))    # 0

# 문제 풀이 시간: 47분

''' 더 좋은 코드
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
'''
