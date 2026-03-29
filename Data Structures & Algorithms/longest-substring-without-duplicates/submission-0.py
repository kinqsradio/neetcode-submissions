class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l, r = 0, 0
        hash_map = {}
        max_len = 0

        while r < len(s): 
            if s[r] in hash_map:
                l = max(l, hash_map[s[r]] + 1)
            max_len = max(max_len, r-l+1)
            hash_map[s[r]] = r
            r+=1

        return max_len
        