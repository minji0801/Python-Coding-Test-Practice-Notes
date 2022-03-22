# 2018 KAKAO BLIND RECRUITMENT > [1차] 비밀지도
# 링크: https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3

'''
1. 각 배열을 이진수로 변환한다.
2. 두 배열을 합한다. 한 곳이라도 1이면 1이다.
3. 최종 배열을 가지고 #과 공백으로 변환한다.
'''
def solution(n, arr1, arr2):
    sum, answer = [], []
    for a, b in zip(arr1, arr2): sum.append(bin(a | b)[2:].zfill(n))
    for s in sum:
        s = s.replace('1', '#')
        s = s.replace('0', ' ')
        answer.append(s)
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))    # ["#####", "# # #", "### #", "#  ##", "#####"]
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))    # ["######", "###  #", "##  ##", " #### ", " #####", "### # "]

# 문제 풀이 시간: 55분
