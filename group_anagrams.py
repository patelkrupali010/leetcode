from collections import defaultdict


class Solution:
    def groupAnagrams(strs):
        ##solution 1
        # map = {}
        # for s in strs:
        #     sorted_word = ''.join(sorted(s))
        #     if sorted_word in map:
        #        map[sorted_word].append(s)
        #     else:
        #         map[sorted_word] = [s]
        # print(list(map.values()))

        ##sol 2
        mapDict = {}
        for s in strs:
            str_arr = [0] * 26
            for i in s:
                str_arr[ord(i) - ord('a')] +=1
            key = '#'.join(str(i) for i in str_arr)
            if key in mapDict:
                mapDict[key].append(s)
            else:
                mapDict[key] = [s]
        return list(mapDict.values())
            

print(Solution.groupAnagrams(["bdddddddddd","bbbbbbbbbbc"]))
