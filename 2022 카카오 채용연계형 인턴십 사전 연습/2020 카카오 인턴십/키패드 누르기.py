def solution(numbers, hand):
    answer = ''

    keypad = {'1': (0,0), '2': (0,1), '3': (0,2), '4': (1,0), '5': (1,1), '6': (1,2), '7': (2,0), '8': (2,1), '9': (2,2), '*': (3,0), '0': (3,1), '#': (3,2)}
    left, right = keypad['*'], keypad['#']

    # 키패드 가운데 줄 숫자 어떤손으로 눌러야할지
    def dd(n):
        h = ''
        xy = keypad[str(n)]
        dl = abs(left[0]-xy[0])+abs(left[1]-xy[1])
        dr = abs(right[0]-xy[0])+abs(right[1]-xy[1])
        
        if dl > dr: h = 'R'
        elif dl < dr:  h = 'L'
        else:
            if hand == "left":  h = 'L'
            else:  h = 'R'

        return [h, xy]

    # 클릭한 손가락과 손의 위치 알아내기
    def click(n):
        xy = keypad[str(n)]
        
        if str(n) in ['1','4','7']:
            return ['L', xy]
        elif str(n) in ['3','6','9']:
            return ['R', xy]
        else:
            return dd(n)
        
    for number in numbers:
        h, xy = click(number)
        answer += h
        
        if h == 'L': left = xy
        else: right = xy
        
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))    # "LRLLLRLLRRL"
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))    # "LRLLRRLLLRR"
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))    # "LLRLLRLLRL"

# 문제 풀이 시간: 39분
