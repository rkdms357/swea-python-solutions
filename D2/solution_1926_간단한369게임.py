N = int(input())
ans = []
for i in range(1, N+1):
    lst = list(map(int, str(i)))
    cnt = lst.count(3) + lst.count(6) + lst.count(9)
    if cnt != 0:
        ans.append('-' * cnt)
    else:
        ans.append(str(i))
print(' '.join(ans))