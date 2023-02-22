
# Two Pointers

# For each char in the input string,
# let two pointers explore both outwards directions, check how long the palindrome could be.

# We need to divide odd case and even case!



class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""

        for i in range(len(s)):
            # odd case, like "bab"
            tmp = self.palindrome(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "baab"
            tmp = self.palindrome(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        
        return res
 
    def palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]