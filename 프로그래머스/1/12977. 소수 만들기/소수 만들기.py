def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    n = len(nums)
    
    # 3중 for문으로 중복 없이 3개의 숫자 선택
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                
                # 고른 3개 숫자의 합
                total_sum = nums[i] + nums[j] + nums[k]
                
                # 소수인지 확인
                if is_prime(total_sum):
                    answer += 1

    return answer