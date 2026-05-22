T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    grid = [input().strip() for _ in range(H)]

    # 격자판 전체가 이미 검은색(#)으로 가득 찬 특수 케이스 처리
    # 행을 다 칠하거나(H) 열을 다 칠하는(W) 것 중 작은 값이 최소 연산
    all_black = True
    for i in range(H):
        if '.' in grid[i]:
            all_black = False
            break

    if all_black:
        print(f"{min(H, W)}")
        continue

    # 일반적인 케이스: 흰색('.')이 섞여있는 경우
    # 전부 '#'인 행의 개수 세기
    row_count = 0
    for i in range(H):
        if '.' not in grid[i]:  # 흰색이 하나도 없다면 행 전체를 칠한 것
            row_count += 1

    # 전부 '#'인 열의 개수 세기
    col_count = 0
    for j in range(W):
        has_white = False
        for i in range(H):
            if grid[i][j] == '.':
                has_white = True
                break
        if not has_white:  # 흰색이 하나도 없다면 열 전체를 칠한 것
            col_count += 1

    # 두 연산 횟수를 더한 것이 최소 연산 횟수
    print(f"{row_count + col_count}")