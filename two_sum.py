
# Create a dictionary to store the index and value

# Iterate through each element in the given array starting from the first element.

# In each iteration check if required number (required  number = target sum - current number) is present in the dictionary.

# If present, return {required number index, current number index} as  result.

# Otherwise add the current iteration number as key and its index as value to the dictionary. Repeat this  until you find the result.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_val_dict = {}
        
        for curr_idx, val in enumerate(nums):
            diff = target - nums[curr_idx]
            
            if diff in idx_val_dict:
                return [curr_idx, idx_val_dict[diff]]
            
            idx_val_dict[val] = curr_idx
        