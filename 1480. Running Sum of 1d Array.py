class Solution:
    def runningSum(nums):
        lst = []
        for i in range(len(nums)):
            lst.append(sum(nums[:i+1]))

        return lst

print(Solution.runningSum([1,2,3,4]))