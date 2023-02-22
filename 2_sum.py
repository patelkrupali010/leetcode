class Solution:
    def twoSum(nums, target):

        ##brute force

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j] 


        # dictMap = {}
        # for idx, val in enumerate(nums):
        #     if val in dictMap:
        #         dictMap[val].append(idx)
        #         return dictMap.values()
        #     else:
        #         dictMap[target-val] = [idx]

        for idx, val in enumerate(nums):
            sec_idx = nums.index(target - val)
            if target - val in nums and sec_idx != idx:
                return [idx,sec_idx]            

            
print(Solution.twoSum([2,7,11,15], 9))