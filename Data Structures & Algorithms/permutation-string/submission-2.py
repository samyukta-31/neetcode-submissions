class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_freq_s1 = [0]*26
        for s in s1:
            char_freq_s1[ord(s)-ord('a')] += 1
        k = len(s1)

        char_freq_s2 = [0]*26

        for s in s2[0:k]:
            char_freq_s2[ord(s)-ord('a')] += 1

        if len(s1) > len(s2):
            return False
        elif char_freq_s1 == char_freq_s2:
            return True
        
        for j in range(k, len(s2)):
            char_freq_s2[ord(s2[j])-ord('a')] += 1
            i = j - k
            char_freq_s2[ord(s2[i])-ord('a')] -= 1
            if char_freq_s1 == char_freq_s2:
                return True
        return False
        