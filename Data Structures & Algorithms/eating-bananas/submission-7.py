class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        l, r = 1, max(piles)
        result = r

        while l <= r:
            k = (l+r) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                result = k
                r = k-1
            else:
                l = k+1
        return result

        # bruteforce
        # speed = 1
        # while True:
        #     hours = 0
        #     for p in piles:
        #         hours += math.ceil(p/speed)
        #     if hours <= h:
        #         return speed
        #     speed += 1

        # return speed