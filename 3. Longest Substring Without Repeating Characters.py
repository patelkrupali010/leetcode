class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = ''
        max_len = 0
		#1. for each character in input string
        for char in s:
			#2. check if char is in temporary string "seen"
            if char not in seen:
			#3. if not seen, add to seen temporary list 
                seen+=char
            #4 if seen, slice seen list to previous char
            # for example, if char is 'a' and seen list is 'abc'
            # you will be slicing previous 'a'(seen.index(char)+1), thus seen list become 'bc'
            # then add the current 'a' at the end of the string.  bc + a, seenlist = 'bca'
            else:
                seen = seen[seen.index(char) + 1:] + char
            #5 check max length between current max with new length of seen
            max_len = max(max_len, len(seen))
        return max_len