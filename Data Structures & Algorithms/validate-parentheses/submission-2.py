class Solution:
    def isValid(self, s: str) -> bool:
        p_hash = {'}':'{',')':'(',']':'['}
        stack = []
        i = 0

        while i<len(s):
            if s[i] in p_hash.values():
                stack.append(s[i])
                i += 1
                continue
            if s[i] in p_hash.keys():
                if stack == []:
                    return False
                if stack.pop(-1) == p_hash[s[i]]:
                    i += 1
                    continue
                else:
                    return False
        if stack != []:
            return False
        return True
        

