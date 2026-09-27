class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        counts_t = {val:0 for val in t}
        len_d_t = len(counts_t)

        for val in t:
            counts_t[val] += 1

        counts_window = {}

        i = 0

        freq = 0

        shortest = None
        for j in range(len(s)):
            counts_window[s[j]]  = counts_window.get(s[j], 0) + 1
            if s[j] in counts_t and counts_window[s[j]] == counts_t[s[j]]:
                freq += 1
            while len_d_t <= freq:
                subs = s[i:j+1]
                if not shortest or len(subs) < len(shortest):
                    shortest = subs
                counts_window[s[i]] -= 1
                if s[i] in counts_t and counts_window[s[i]] < counts_t[s[i]]:
                    freq -= 1
                i += 1
                
            
        return shortest if shortest else ""



            