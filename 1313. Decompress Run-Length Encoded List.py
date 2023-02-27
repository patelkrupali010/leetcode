class Solution:
    def decompressRLElist(nums):
        # res = []
        # freq = 0
        # val = 0
        # for i in range(len(nums)//2):
        #     print("i: ", i)
        #     freq = nums[2*i]
        #     val = nums[2*i + 1]
        #     res = res + [val] * freq
        #     i = i+2
        # return res

        #optimized soln
        res=[]
        for i in range(0,len(nums),2):
            res+=[nums[i+1]]*(nums[i])
        return res

print(Solution.decompressRLElist([1,2,3,4]))