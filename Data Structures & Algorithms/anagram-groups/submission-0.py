class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_hash = {''.join(sorted(s)): [] for s in strs}

        for s in strs:
            sorted_hash[''.join(sorted(s))].append(s)

        return [val for val in sorted_hash.values()]