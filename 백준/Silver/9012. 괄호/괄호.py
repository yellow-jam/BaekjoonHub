def check(str):
    check = 1
    for i in range(len(str)):
        if(str[i]=='('):
            check+=1
        else:
            check-=1

        if (check==0):
            return "NO"

    if (check == 1):
        return "YES"
    return "NO"

## 메인 ##
import sys

N=int(sys.stdin.readline().strip())

for i in range(N):
    str = sys.stdin.readline().strip()
    print(check(str))