# 링크: https://codeup.kr/problem.php?id=1807

'''
1, 어떤 자연수 n이 입력되면,
2. n이 홀수이면 3n+1을 하고,
3. n이 짝수이면 n/2를 한다.
4. 이 n이 1이 될때까지 2~3과정을 반복한다.
'''
# a에서 b사이에 길이가 가장긴 우박수와 그 길이를 출력한다. 
# 만약 가장 긴 수가 두 개이상인 경우, 작은 숫자를 출력하시오.

# a, b = 1, 10

a, b = map(int, input().split())

dic = dict()
for n in range(a, b+1):
    k = n
    count = 1
    while n != 1:
        if n % 2 != 0: n = 3 * n + 1
        else: n /= 2
        count += 1
        
    dic[k] = count

hail = min([k for k,v in dic.items() if v == max(dic.values())])
print(hail, dic[hail])

# 문제 풀이 시간: 15분
