T = int(input())
for test_case in range(1, T+1):
    lst = list(map(int, input().split()))
    ans = []
    mx = 0
    for i in range(len(lst)-2):
        for j in range(i+1, len(lst)-1):
            for k in range(j+1, len(lst)):
                ans.append(lst[i]+lst[j]+lst[k])
    ans.sort(reverse = True)
    ans = list(set(ans))
    print(f'#{test_case}', ans[4])