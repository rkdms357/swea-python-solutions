def solve():
    for i in range(len(lst2)):
        lst2[i] = (lst2[i]+1)%2
        # 2진수를 10진수로
        num = 0
        for n in lst2:
            num = num * 2 + n
        # 10진수를 3진수로
        tlst, t = [], num
        while t > 0:
            tlst.insert(0, t % 3)
            t //= 3
        r1, r2, cnt = tlst[::-1], lst3[::-1], 0
        for j in range(min(len(tlst), len(lst3))):
            if r1[j] != r2[j]:
                cnt += 1
        cnt += abs(len(r1) - len(r2))
        if cnt == 1:
            return num
        lst2[i] = (lst2[i]+1)%2
T = int(input())
for test_case in range(1, T+1):
    lst2 = list(map(int, input()))
    lst3 = list(map(int, input()))
    # 모든 자릿수를 하나씩 바꿔가면서 비교
    ans = solve()
    print(f'#{test_case}', ans)