class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort 1
        # if len(s) != len(t): return False

        # for c in set(s):
        #     if s.count(c) != t.count(c):
        #         return False

        # return True
        
        # Sort 2
        # if len(s) != len(t): return False
        # return sorted(s) == sorted(t)

        # Hashmap
        if len(s) != len(t): return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS==countT