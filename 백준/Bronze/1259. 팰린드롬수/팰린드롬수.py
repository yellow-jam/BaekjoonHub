while True:
    ss=input()
    if ss=='0':
        break
    elif ss==ss[::-1]:
        print("yes")
    else:
        print("no")
