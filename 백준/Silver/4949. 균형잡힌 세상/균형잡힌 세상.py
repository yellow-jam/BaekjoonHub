import sys
input = sys.stdin.readline

while True:
    ss = input().rstrip()
    if ss == ".":
        break

    stack = []
    flag = 1

    for i in ss:
        if i == '(' or i == '[':
            stack.append(i)
        if i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = 0
                break
        if i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = 0
                break

    print("yes" if flag and not (stack) else "no")
