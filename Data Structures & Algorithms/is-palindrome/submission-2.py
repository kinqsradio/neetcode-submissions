
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s=re.sub(r'[^a-zA-Z0-9]', '', s)
        clean_s=clean_s.lower()
        # return clean_s==clean_s[::-1]

        left, right = 0, len(clean_s)-1
        while left < right:
            if clean_s[left] != clean_s[right]:
                return False

            left, right = left+1, right-1

        return True