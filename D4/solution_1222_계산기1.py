T = 10
for test_case in range(1, T+1):
    input()
    st = input()
    equ = ''
    stk = []
    for ch in st:
        if ch.isdigit():
            equ += ch
        else:
            if not stk:
                stk.append(ch)
            else:
                while stk:
                    equ += stk.pop()
                stk.append(ch)
    while stk:
        equ += stk.pop()
    for ch in equ:
        if ch.isdigit():
            stk.append(int(ch))
        else:
            op2 = stk.pop()
            op1 = stk.pop()
            stk.append(op2+op1)
    print(f'#{test_case}', stk.pop())