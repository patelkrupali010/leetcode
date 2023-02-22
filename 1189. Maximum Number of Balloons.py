class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        h=dict({'b':0,'a':0,'l':0,'o':0,'n':0})
        for i in text: 
            if i in ['b','a','l','o','n']:
                h[i]+=1
        h['o']//=2
        h['l']//=2
        return min(h.values())