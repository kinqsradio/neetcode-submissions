from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # The reason for us to sort is we need to pop the 2 heaviest stone
        stones.sort() 
        n = len(stones)

        while n > 1:
            cur = stones.pop() - stones.pop() # heaviest1 - heaviest2
            n -= 2 # decrease total stones by 2 since we used 2 stones

            if cur > 0:
                l, r = 0, n
                while l < r:
                    mid = (l+r) // 2
                    if stones[mid] < cur:
                        l = mid +1
                    else:
                        r = mid
                pos = l
                n += 1
                stones.append(0)
                for i in range(n-1, pos, -1):
                    stones[i] = stones[i-1]
                stones[pos] = cur

        return stones[0] if n > 0 else 0