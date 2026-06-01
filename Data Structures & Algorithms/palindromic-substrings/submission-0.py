class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j 
                while l<r and s[l] ==s[r]:
                    l+=1
                    r-=1
                res += (l>=r)
        
        return res