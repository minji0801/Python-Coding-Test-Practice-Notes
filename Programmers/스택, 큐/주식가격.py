# 스택/큐 > 주식가격
# 링크: https://programmers.co.kr/learn/courses/30/lessons/42584

# 초 단위로 기록된 주식가격이 담긴 배열 prices
# 가격이 떨어지지 않은 기간은 몇 초인지를 return
def solution(prices):
    answer = []

    # 가격이 떨어질 때까지 반복문 돌리기
    for i in range(len(prices)-1):
        s = 0
        for j in range(i+1, len(prices)):
            s += 1
            if prices[i] > prices[j]: break
        answer.append(s)

    # 어차피 마지막은 0
    answer.append(0)
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([1,2,3,2,3]))    # [4,3,1,1,0]

# 문제 풀이 시간: 21분

''' 더 좋은 풀이
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
'''
