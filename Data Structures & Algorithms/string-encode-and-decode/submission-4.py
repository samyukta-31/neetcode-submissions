class Solution:
    def encode(self, strs: List[str]) -> str:
        self.h = {}
        import string

        # Combine lowercase, uppercase, digits, and punctuation
        char = list(
            string.ascii_lowercase + 
            string.ascii_uppercase + 
            string.digits + 
            string.punctuation + " "
        )
        enc = ""
        for word in strs:
            for s in word:
                try:
                    print(s)
                    enc+=char[char.index(s)+1]
                except IndexError:
                    enc+=char[0]
        self.h[enc] = strs
        return enc

    def decode(self, s: str) -> List[str]:
        return self.h[s]
