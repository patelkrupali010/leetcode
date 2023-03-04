class Solution:
    def maxNumberOfBalloons(text: str) -> int:
        h={'b':0,'a':0,'l':0,'o':0,'n':0}
        for i in text: 
            if i in h:
                h[i]+=1
        h['o']//=2
        h['l']//=2
        return min(h.values())
    
print(Solution.maxNumberOfBalloons("nlaebolkovballoon"))