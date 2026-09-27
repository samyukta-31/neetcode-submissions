class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for i in range(len(nums))]
        prod = 1
        num_zeroes = 0
        for num in nums:
            if num!= 0:
                prod *= num
            else:
                num_zeroes += 1
                continue

        for i, num in enumerate(nums):
            if num_zeroes > 1:
                output[i] = 0
            elif num_zeroes == 1 and num == 0:
                output[i] = prod
            elif num_zeroes == 1 and num != 0:
                output[i] = 0
            else:
                output[i] = int(prod/num)
        
        return output
        