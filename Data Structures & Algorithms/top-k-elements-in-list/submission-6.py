class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter = Counter(nums)
        # heap = []

        # for num, count in counter.items():
        #     heapq.heappush(heap, (count, num))

        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # res = []
        # while heap:
        #     res.append(heapq.heappop(heap)[1])

        # return res

        """
        Bucket Sort
        """
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

        return result