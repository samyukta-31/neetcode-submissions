class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_s = set(nums)
        start_seq = set()
        max_cons = 1
        cons = 1

        for num in num_s:
            if num + 1 in num_s and num - 1 not in nums:
                start_seq.add(num) 
        
        print(start_seq)
        for start in start_seq:
            val = start
            while val + 1 in num_s:
                cons += 1
                val += 1
            else:
                max_cons = max(max_cons, cons)
                cons = 1
        max_cons = max(max_cons, cons)

        return max_cons

        