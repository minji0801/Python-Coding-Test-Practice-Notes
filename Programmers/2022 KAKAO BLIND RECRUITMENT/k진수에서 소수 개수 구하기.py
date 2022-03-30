# 2022 KAKAO BLIND RECRUITMENT > k진수에서 소수 개수 구하기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/92335?language=python3

def solution(n, k):
    arr = convert(n, k).split('0')
    arr = list(filter(lambda x: x != '1', arr))
    arr = list(filter(lambda x: x != '', arr))
    answer = len(arr)

    for i in arr:
        for j in range(2, int(int(i)**0.5)+1):
            if int(i) % j == 0: 
                answer -= 1
                break
    return answer 

def convert(n, k):
    answer = ''
    while n > 0:
        n, mod = divmod(n, k)
        answer += str(mod)
    return answer[::-1] 

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(437674, 3))    # 3
print(solution(110011, 10))    # 2
print(solution(12, 10))

# 문제 풀이 시간: 36분
