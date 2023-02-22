# Get the leftmost index such that sum of value till that index equals sum of values beyond that index.

# Initialise the left portion sum (s1) by 0 and the right portion sum (s2) by the sum of given list.

# Iterate through the list, each time decrease the value of s2 by value present at current index.

# Check for the equality of the two sums....if equal return the current index as answer.

# If not equal, increment the value of s1 by the the value at current index.

# This process will continue untill the value of s1 equals value of s2.

# If the values aren't equal then at outside of loop return -1.




class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s1,s2=0,sum(nums)
        for i in range(len(nums)):
            s2-=nums[i]
            if s1==s2:
                return i
            s1+=nums[i]
        return -1