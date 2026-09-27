class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sh = {l:0 for l in s}
        th = {l:0 for l in t}

        for l in s:
            sh[l] += 1
        for l in t:
            th[l] += 1
        
        return sh == th