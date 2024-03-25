class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ind = 0
        merged = ""
        while ind < len(word1) or ind < len(word2):
            if ind < len(word1):
                merged += word1[ind]
            if ind < len(word2):
                merged += word2[ind]
            ind += 1
        return merged
