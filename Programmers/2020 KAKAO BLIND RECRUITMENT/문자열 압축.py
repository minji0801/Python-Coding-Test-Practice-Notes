# 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이

def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)+1):
        string, count = [], []
        prev = ''
        
        for j in range(0, len(s), i):
            a = s[j:j+i]
            if prev != a:
                string.append(a)
                count.append(1)
            else:
                count[-1] += 1
            prev = a

        for i in range(len(count)):
            if count[i] == 1:
                count[i] = ''
            else:
                count[i] = str(count[i])
        
        res = ''.join(map(''.join, zip(map(str, count), string)))
        answer = min(answer, len(res))
        
    return answer

print(solution("aabbaccc"))    # 7
print(solution("aaaaaaaaaaaabcd"))    # 6
print(solution("xxxxxxxxxxyyy"))    # 5

# 문제 풀이 시간: 32분
