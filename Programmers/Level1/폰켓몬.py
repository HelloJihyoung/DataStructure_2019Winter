def solution(nums):
    sort = len(set(nums))
    if sort < len(nums) // 2:
        return sort
    return len(nums) // 2

nums = [3,3,3,2,2,4]
print(solution(nums))