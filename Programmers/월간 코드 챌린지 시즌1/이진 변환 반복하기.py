# 월간 코드 챌린지 시즌1 > 이진 변환 반복하기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/70129

'''
1. x의 모든 0을 제거합니다.
2. x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
3. x가 "1"이 될 때까지 계속
return [이진 변환 횟수, 변환 과정에서 제거된 모든 0의 개수]
'''

# 1. 0을 제거하는데, 제거된 0의 개수를 저장해야 한다.
# 2. 0을 제거한 문자열이 "1"인지 확인한다.
# 3. "1"이 아니면 계속 반복하고, 이진 변환 횟수를 저장해야 한다.
def solution(s):
    answer = [0, 0]
    while s != '1':
        answer[0] += 1               # 이진 변환 횟수 카운트
        answer[1] += s.count('0')    # 제거할 0의 개수 카운트
        s = s.replace('0', '')
        s = format(len(s), 'b')
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("110010101001"))    # [3, 8]
print(solution("01110"))    # [3, 3]
print(solution("1111111"))    # [4, 1]

# 문제 풀이 시간: 15분

''' 더 좋은 풀이
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]
'''

# 반복문 돌 때마다 배열에 접근하면 당연히 시간이 더 오래걸린다.
