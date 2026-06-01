class Solution:
    def countSubstrings(self, s: str) -> int:
        # bruteforce
        # res = 0

        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         l, r = i, j 
        #         while l<r and s[l] ==s[r]:
        #             l+=1
        #             r-=1
        #         res += (l>=r)
        
        # return res

        # 2 pointers
        res = 0
        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res+=1
                l-=1
                r+=1

            # even
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res+=1
                l-=1
                r+=1
        return res