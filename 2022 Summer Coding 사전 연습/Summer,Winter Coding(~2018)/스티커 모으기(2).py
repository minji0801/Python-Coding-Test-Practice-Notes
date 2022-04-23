def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    
    a = sticker[1:]
    b = sticker[:-1]

    i = 1
    while i < len(sticker)-1:
        if i == 1:
            a[i] = max(a[i-1], a[i])
            b[i] = max(b[i-1], b[i])
        else:
            a[i] = max(a[i-1], a[i-2]+a[i])
            b[i] = max(b[i-1], b[i-2]+b[i])
        i += 1

        print(a)

    return max(a[-1], b[-1])

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))    # 36
print(solution([1, 3, 2, 5, 4]))    # 8
print(solution([1])) # 1
