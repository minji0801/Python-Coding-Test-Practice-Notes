# 2021 Dev-Matching: 웹 백엔드 개발자(상반기) > 로또의 최고 순위와 최저 순위
# 링크: https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3

'''
1	6개 번호가 모두 일치
2	5개 번호가 일치
3	4개 번호가 일치
4	3개 번호가 일치
5	2개 번호가 일치
6(낙첨)	그 외
'''
# 알아볼 수 없는 번호를 0으로 표기
# 로또 번호를 담은 배열 lottos, 당첨 번호를 담은 배열 win_nums
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    right, unknown = 0, 0
    for n in lottos:
        if n == 0: unknown += 1
        else: 
            if n in win_nums: right += 1

    return [rank[right + unknown], rank[right]]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))    # [3, 5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))    # [1, 6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))    # [1, 1]

# 문제 풀이 시간: 13분

''' 더 좋은 풀이
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
'''
