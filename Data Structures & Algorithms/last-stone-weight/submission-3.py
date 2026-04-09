from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) > 1:
            stones.sort(reverse=True)
            x = stones.pop(0)  # heaviest
            y = stones.pop(0)  # second heaviest
            if x != y:
                # insert the difference back keeping order
                diff = x - y
                # insert diff to keep list sorted in descending order
                # find position to insert
                stones.insert(1, diff)
        return stones[0] if stones else 0