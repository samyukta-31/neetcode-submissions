class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted([l for l in s]) == sorted([l for l in t])