# 2020 카카오 인턴십 > 키패드 누르기
# 링크: https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

# numbers: 순서대로 누를 번호, hand: 어느 손 잡이인지
def solution(numbers, hand):
    left, right = [3, 0], [3, 2]
    answer = ''

    for i in numbers:
        c = findLocation(i)    # 눌러야 하는 숫자의 키패드 위치
        
        if i == 1 or i == 4 or i == 7 :    # 왼손으로 누르기
            answer += "L"
            left = c
        elif i == 3 or i == 6 or i == 9:    # 오른손으로 누르기
            answer += "R"
            right = c
        else:
            clickedHand = whereIsColser(c, left, right, hand)
            if clickedHand == "L":
                answer += "L"
                left = c
            elif clickedHand == "R":
                answer += "R"
                right = c
    
    return answer

# 키패드 위치 구하기
def findLocation(i):
    keypad = {0: [1, 2, 3], 1: [4, 5, 6], 2: [7, 8, 9], 3: [-1, 0, -2]}
    for key, value in keypad.items():
        if i in value :
            return [key, value.index(i)]

# 더 가까운 손 구하기
def whereIsColser(t, l, r, hand):
    left = abs(t[0] - l[0]) + abs(t[1] - l[1])
    right = abs(t[0] - r[0]) + abs(t[1] - r[1])

    if left < right:    # 왼손으로 누르기
        return "L"
    elif right < left:    # 오른손으로 누르기
        return "R"
    else:    # 어떤 손 잡이인지에 따라
        if hand == "left": return "L"
        elif hand == "right": return "R"
        
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))    # "LRLLLRLLRRL"
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))    # "LRLLRRLLLRR"
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))    # "LLRLLRLLRL"

# 문제 풀이 시간: 42분

''' 더 좋은 코드
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer
'''
