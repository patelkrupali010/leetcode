class Solution:
    def smallerNumbersThanCurrent(nums):
        temp = sorted(nums)
        res = []
        # prev_num = temp[0] #1
        # map = {}
        
        # for i in range(1,len(temp)):
        #     if prev_num == temp[i]:
        #         temp[i] = temp[i-1] #[0,2,2,5]
        #         # map[temp[i]] = temp[i-1] #[0,2,2,5]
        #     else:
        #         prev_num = temp[i]
        #         temp[i] = len(temp[:i])
        #         # map[temp[i]] = len(temp[:i])
        # return temp

        for i in nums:
            res.append(temp.index(i))
        return res



    

print(Solution.smallerNumbersThanCurrent([8,1,2,2,3]))