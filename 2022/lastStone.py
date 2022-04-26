class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) >1:
            firstMaxStone = max(stones)
            stones.remove(firstMaxStone)
            if stones:
                secondMaxStone = max(stones)
                stones.remove(secondMaxStone)
           
            remaining = abs(firstMaxStone - secondMaxStone)
            stones.append( remaining)
                
        if len(stones):
            return stones[0]
        else:
            return 0 