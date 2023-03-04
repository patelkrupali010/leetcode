class Solution:
    def sumOddLengthSubarrays(arr):
        result = 0
        length = len(arr)
        for idx, val in enumerate(arr):
            start = length - idx
            end = idx + 1
            total = start * end + 1
            odd = total // 2
            result += odd * val
        return result 

print(Solution.sumOddLengthSubarrays([1,4,2,5,3]))



