
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s=re.sub(r'[^a-zA-Z0-9]', '', s)
        clean_s=clean_s.lower()
        return clean_s==clean_s[::-1]