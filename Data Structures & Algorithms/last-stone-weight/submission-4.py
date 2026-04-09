from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x = stones.pop() # heaviest1
            y = stones.pop() # heaviest2   
            if x != y:
                diff = x - y
                stones.append(diff)         

        return stones[0] if stones else 0