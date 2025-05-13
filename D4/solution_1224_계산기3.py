icp = {'(':3, '*':2, '+':1}
isp = {'*':2, '+':1, '(':0}
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
            if ch == ')':
                while stk:
                    t = stk.pop()
                    if t == '(':
                        break
                    else:
                        equ += t
            else:
                while stk and icp[ch] <= isp[stk[-1]]:
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
            if ch == '*':
                stk.append(op2*op1)
            elif ch == '+':
                stk.append(op2+op1)
    print(f'#{test_case}', stk.pop())