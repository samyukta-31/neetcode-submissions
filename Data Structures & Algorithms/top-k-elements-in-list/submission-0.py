class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        nums_dict = {num:0 for num in nums}
        for num in nums:
            nums_dict[num] += 1
        print(nums_dict)
        h = []
        heapq.heapify(h)

        i = 0
        for key, value in nums_dict.items():
            heapq.heappush(h, (value, key))

        print(h)

        while i<len(nums_dict)-k:
            heapq.heappop(h)
            print(h)
            i+=1
        print(h)

        # return [0,0]
        return [val[1] for val in h]