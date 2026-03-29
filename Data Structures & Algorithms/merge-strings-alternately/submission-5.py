class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1) , len(word2)
        i = j = 0
        result = []

        while i < n or j < m:
            if i < n:
                result.append(word1[i])
            if j < m:
                result.append(word2[j])

            i, j = i+1, j+1

        return ''.join(result)

        