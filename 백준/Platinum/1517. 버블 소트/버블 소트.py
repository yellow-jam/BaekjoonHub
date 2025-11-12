import sys
input = sys.stdin.readline
result = 0


def merge_sort(s, e):
    global result

    if e-s < 1: return  # 더는 자를 수 없을 때 리턴
    m = int(s+(e-s) / 2)
    merge_sort(s,m)
    merge_sort(m+1,e)
    for i in range(s, e+1):
        tmp[i] = A[i]

    k = s  # 어느 위치에 데이터가 들어가야 하는지 나타내는 인덱스
    index1 = s
    index2 = m+1
    while index1 <=m and index2 <= e:  # 두 그룹을 합쳐주는 로직
        if tmp[index1] > tmp[index2]:  # 앞의 데이터가 큰 경우, 뒤의 데이터가 앞으로 옴
            A[k] = tmp[index2]
            result = result + index2 - k  # swap 값 카운트 = 뒷그룹의인덱스 - k = 앞그뤂에 남아있는 데이터의 개수 = 역전한 개수
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]  # 앞의 데이터가 선택된 경우, k만 늘어남
            k += 1
            index1 += 1

    # 각 그룹에서, 남은 뒤쪽 데이터
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1


N = int(input())
A = list(map(int, input().split()))
A.insert(0,0)  # 0번째 인덱스는 신경쓰지 않으려고
tmp = [0] * int(N+1)  # A배열의 크기와 동일
merge_sort(1,N)
print(result)
