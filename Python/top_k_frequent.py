class Solution:
    def topKFrequent(nums, k):
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        
        lst=[]
        for key, val in map.items():
            lst.append()






print(Solution.topKFrequent([1,1,1,2,2,3], 2))
