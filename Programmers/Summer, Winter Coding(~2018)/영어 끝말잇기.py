# Summer/Winter Coding(~2018) > 영어 끝말잇기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/12981

# 사람의 수 n과 사람들이 순서대로 말한 단어 words
# [가장 먼저 탈락하는 사람의 번호, 그 사람이 자신의 몇 번째 차례에 탈락하는지]
# 탈락자가 생기지 않는다면 [0, 0]


# 앞 단어의 마지막 문자로 시작하는 단어가 아니거나 이전에 등장했던 단어를 말하면 탈락
def solution(n, words):
    answer = [0, 0]

    for i in range(1, len(words)):
        if (words[i-1][-1] != words[i][0]) or (words[i] in words[:i]):
            turn, num = divmod(i, n)
            answer[0] = num+1
            answer[1] = turn+1
            break

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))    # [3, 3]
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))    # [0,0]
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))    # [1,3]

# 문제 풀이 시간: 21분

''' 더 좋은 풀이
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
'''
