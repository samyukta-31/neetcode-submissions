class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0
        chars = set(s)

        for c in chars:
            count = 0
            i = 0
            for j in range(len(s)):
                if s[j] == c:
                    count += 1
                while (j - i + 1) - count > k:
                    if s[i] == c:
                        count -= 1
                    i += 1
                max_count = max(max_count, j - i + 1)
        
        return max_count
            
