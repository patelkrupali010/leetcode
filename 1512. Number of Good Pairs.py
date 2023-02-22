class Solution:
    def numIdenticalPairs(nums):
       ## brute force
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j] and i<j:
        #             count += 1
        # return count

        ## hashmap and math combinations
        # map = {}
        # for num in nums:
        #     if num in map:
        #         map[num] += 1
        #     else:
        #         map[num] = 1
        # count = 0
        # for value in map.values():
        #     count += (value * (value - 1)) / 2
        # return count

        ##hashmap
        map = {}
        res = 0
        for num in nums:
            if num in map:
                res += map[num]
                map[num] += 1
            else:
                map[num] = 1
        return res

print(Solution.numIdenticalPairs([1,2,3,1,1,3]))