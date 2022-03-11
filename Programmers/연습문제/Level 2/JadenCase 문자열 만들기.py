# 연습문제 > JadenCase 문자열 만들기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3

# 모든 단어의 첫 문자가 대문자고, 그 외의 알파벳은 소문자
def solution(s):
    return ' '.join([w[0].upper()+w[1:] if w != '' else '' for w in s.lower().split(' ')])

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("3people unFollowed me"))    # "3people Unfollowed Me"
print(solution("for the last week"))    # "For The Last Week"
print(solution("a a a a a a a "))    # A A A A A A A 

# 문제 풀이 시간: 22분

''' 문제가 개편되어 오답이지만 새로 알게 된 코드
def Jaden_Case(s):
    return s.title()
'''
