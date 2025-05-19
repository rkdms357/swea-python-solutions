T = int(input())
for test_case in range(1, T+1):
    st = list(input())
    st.sort()
    for i in range(len(st)-1):
        for j in range(i+1, len(st)):
            if st[i] == st[j]:
                st[i] = st[j] = ''
    ans = ''.join(st)
    if ans == '':
        print(f'#{test_case}', 'Good')
    else:
        print(f'#{test_case}', ans)