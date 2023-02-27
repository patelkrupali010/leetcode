class Solution:
    def createTargetArray(nums, index):
        # map = {}
        # for i in range(len(index)):
        #     if index[i] in map:
        #         map[index[i]].append(nums[i])
        #     else:
        #         map[index[i]] = [nums[i]]



        # return [i for i in map.values()]

        lst = [] 
        for i in range(len(index)):
                lst.insert(index[i], nums[i])
        return lst
        

print(Solution.createTargetArray([0,1,2,3,4], [0,1,2,2,1]))