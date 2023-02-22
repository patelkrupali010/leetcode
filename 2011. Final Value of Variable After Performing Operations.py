class Solution:
    def finalValueAfterOperations(operations):
        ##sol1
        # map = {"++X":1, "X++": 1, "--X": -1, "X--": -1}
        # res = 0
        # for s in operations:
        #     res = res + map[s]
        #     print(res)
        # return res

        ##sol2
        # res = 0
        # for s in operations:
        #     if s in ["++X", "X++"]:
        #         res = res + 1
        #     else:
        #         res = res - 1
        # return res

        ##sol3
        res = 0
        for s in operations:
            if '+' in s:
                res+=1
            else:
                res-=1
        return res

print(Solution.finalValueAfterOperations(["--X","X++","X++"]))