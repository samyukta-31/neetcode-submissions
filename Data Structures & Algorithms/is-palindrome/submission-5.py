class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = ""

        for val in s:
            if val.isalnum():
                alnum += val.lower()
        print(alnum)
        i = 0
        j = len(alnum) - 1

        while i<j:
            if alnum[i] == alnum[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
            