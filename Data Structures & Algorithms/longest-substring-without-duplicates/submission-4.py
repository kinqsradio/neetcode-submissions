class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0

        l, r = 0, 0
        hash_map = {}
        max_len = 0

        for r in range(len(s)): 
            if s[r] in hash_map:
                # Update Position of Left Pointer
                l = max(l, hash_map[s[r]] + 1)
            max_len = max(max_len, r-l+1) # Update Max Length
            hash_map[s[r]] = r # Add it to hashmap
            r+=1

        return max_len
        