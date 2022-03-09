# 연습문제 > 이상한 문자 만들기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3

def solution(s):
    words = [w for w in list(s.upper().split(' '))]
    for i in range(len(words)):
        word = list(words[i])
        for j in range(len(word)):
            if j % 2 != 0:
                word[j] = word[j].lower()
        words[i] = ''.join(word)
    return ' '.join(words)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("try hello world"))    # "TrY HeLlO WoRlD"

# 문제 풀이 시간: 26분

''' 더 좋은 코드
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
'''
