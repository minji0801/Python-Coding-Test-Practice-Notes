# 가장 먼저 탈락하는 사람의 번호와 몇 번째 차례에서 탈락했는지

def solution(n, words):
    for i in range(1,len(words)):
        num, round = i%n+1, i//n+1
        prev, now = words[i-1], words[i]
        
        if now in words[:i-1] or prev[-1] != now[0]:
            return [num, round]

    return [0,0]
        
    # 앞 단어의 마지막 문자로 시작해야한다.
    # 이전에 등장한 단어는 사용할 수 없다.


print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))    # [3,3]
print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))    # [0,0]
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))    # [1,3]

# 문제 풀이 시간: 18분
