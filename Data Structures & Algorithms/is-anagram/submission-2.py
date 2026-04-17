class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort 1
        # if len(s) != len(t): return False

        # for c in set(s):
        #     if s.count(c) != t.count(c):
        #         return False

        # return True
        
        # Sort 2
        if len(s) != len(t): return False
        return sorted(s) == sorted(t)