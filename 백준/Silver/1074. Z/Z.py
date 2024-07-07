def visit(N, r, c):
    if N == 0:
        return 0

    n1 = 1 << (N - 1)
    n2 = 1 << N
    small = n1 * n1

    if r < n1 and c < n1:  # 2분면
        return visit(N - 1, r, c)
    elif r < n1 and n1 <= c < n2:  # 1분면
        return small + visit(N - 1, r, c - n1)
    elif n1 <= r < n2 and c < n1:  # 3분면
        return small * 2 + visit(N - 1, r - n1, c)
    else:  # 4분면
        return small * 3 + visit(N - 1, r - n1, c - n1)


N, r, c=map(int, input().split())
    
print(visit(N, r, c))
