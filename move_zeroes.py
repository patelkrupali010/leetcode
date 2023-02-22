def move_zero(nums):
    zero = 0 #for keeping records of zeroes
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zero], nums[i] = nums[i], nums[zero] #swap zero and non-zero elements if current number in input list is non-zero
            zero += 1
    print(nums)


nums = [0,1,0,3,12]
move_zero(nums)


#solution 2 - better solution

# 1. start from end of list to start element
# 2. check if current num is 0
# 3. pop if zero element
# 4. and append 0 to the end



# def move_zero(nums):
#     for i in range(len(nums))[::-1]:
#         if nums[i] == 0:
#             nums.pop(i)
#             nums.append(0)


# nums = [0,1,0,3,2,12]
# move_zero(nums)