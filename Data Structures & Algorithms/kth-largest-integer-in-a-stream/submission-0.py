class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr=nums
        self.k = k
        

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[len(self.arr)-self.k]
