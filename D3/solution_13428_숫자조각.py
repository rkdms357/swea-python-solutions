T = int(input())
for test_case in range(1, T+1):
    lst = list(input())
    mx, mn = ''.join(lst), ''.join(lst)
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            lst[i], lst[j] = lst[j], lst[i]
            tlst = ''.join(lst)
            if tlst > mx:
                mx = tlst
            if tlst[0] != '0' and tlst < mn:
                mn = tlst
            lst[i], lst[j] = lst[j], lst[i]
    print(f'#{test_case}', mn, mx)