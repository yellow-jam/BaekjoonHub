import sys

stack=[]  # 스택
ascend = 1  # 오름차순
answer = ""
flag = 0

N=int(sys.stdin.readline().strip())

for i in range(N):
    num = int(sys.stdin.readline().strip())
    while num>=ascend:
        stack.append(ascend)
        answer += "+\n"
        ascend += 1
    if (num==stack[-1]):
        stack.pop()
        answer += "-\n"
    else:
        print("NO")
        flag = 1
        break
if flag == 0:
    print(answer.strip())