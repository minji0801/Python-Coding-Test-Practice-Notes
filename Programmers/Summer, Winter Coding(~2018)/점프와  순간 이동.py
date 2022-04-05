# Summer/Winter Coding(~2018) > 점프와 순간 이동
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    ans = 0
    
    while n > 0:
        s, r = divmod(n, 2)
        n = s
        ans += r

    return ans

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(5))    # 2
print(solution(6))    # 2
print(solution(5000))    # 5

# 질문하기 참고

''' 더 좋은 풀이
def solution(n):
    return bin(n).count('1')
'''
