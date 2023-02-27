# def isAnagram(s, t):
#     if sorted(s) == sorted(t):
#         return True
#     else:
#         return False

# isAnagram("aana", "naaa")

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = all(s.count(c) == t.count(c) for c in set(s+t)) # 99.27% memory 96.50%
        print(res)


Solution.isAnagram(Solution, "anagram", "nagaram")