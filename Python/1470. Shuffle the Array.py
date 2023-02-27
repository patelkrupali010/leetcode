class Solution:
    def shuffle(nums, n):
        x = 0
        y = n
        res = []
        while x < n:
            res.append(nums[x])
            res.append(nums[y])
            x+=1
            y+=1
        return res

print(Solution.shuffle([2,5,1,3,4,7], 3))