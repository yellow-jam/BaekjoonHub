N, M = map(int, input().split())
ans = []

def back():
    if len(ans) == M:  # 배열의 길이를 확인(재귀함수를 마치는 조건)
        print(' '.join(map(str, ans)))
        return

    for i in range(1, N + 1):  # 1 ~ N 까지
        if i not in ans:  # 중복 확인(백트래킹에서의 한정 조건)
            ans.append(i)  # 배열 추가
            back()  # 재귀
            ans.pop()  # return으로 돌아오면 이게 실행됨. [1, 2, 3]일 때 3을 pop해서 전 단계로 돌아가는 것
    return

back()