def maxSubArray(nums):
    tot_sum = max_sum = nums[0]
    for i in nums[1:]:
        tot_sum = max(tot_sum + i, i)
        max_sum = max(tot_sum, max_sum)
    print(max_sum)

nums = [3,4,5,-1,5,9]
maxSubArray(nums)