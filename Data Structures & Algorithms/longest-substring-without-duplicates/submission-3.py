class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        max_subs = 0
        done = set()

        for j in range(len(s)):
            print(s[j], s[i], j, i)
            while s[j] in done:
                done.remove(s[i])
                i += 1
            done.add(s[j])
            max_subs = max(max_subs, j + 1 - i)

        return max_subs