class Solution:
    def differenceOfSum(nums):
        # return sum(nums) - sum(int(s) for i in nums for s in str(i) )
        digit = 0
        total_sum = 0
        for num in nums:
            total_sum += num
            while num:
                digit = digit + num % 10  #quotient eg: 15, num%10=5
                num = num//10             #remainder num//10=1

        return abs(total_sum - digit)

 


print(Solution.differenceOfSum([1,15,6,3]))