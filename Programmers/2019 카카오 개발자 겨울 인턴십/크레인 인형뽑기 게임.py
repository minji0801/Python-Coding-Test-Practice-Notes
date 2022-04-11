# 2019 카카오 개발자 겨울 인턴십 > 크레인 인형뽑기 게임
# 링크: https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3

# 사라진 인형 수 return
def solution(board, moves):
    count = 0
    basket = [0]
    dic = {i:[] for i in range(1, len(board)+1)}

    for b in reversed(board):
        for i, n in enumerate(b):
            if n != 0: dic[i+1].append(n)

    for m in moves:
        if dic[m]:
            n = dic[m].pop()
            if n == basket[-1]:
                basket.pop()
                count += 2
                continue
            basket.append(n)

    return count

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))    # 4

# 문제 풀이 시간: 26분

''' 더 좋은 코드
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
'''
