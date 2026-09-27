class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid
        r = l - 1 if l != 0 else len(nums) - 1

        print(target, nums[l], nums[0], nums[r], nums[-1])
        print(target >= nums[l] and target < nums[0])
        if target >= nums[l] and target < nums[0]:
            # segment = nums[l:]
            i = l
            j = len(nums) - 1
        # elif target <= nums[r] and target > nums[-1]:
            # segment = nums[:r+1]
            # i = 0
            # j = r
        else:
            i = 0
            j = r
        # print(segment)
        
        while i <= j:
            new_mid = i + (j - i)//2
            if target > nums[new_mid]:
                i = new_mid + 1
            elif target < nums[new_mid]:
                j = new_mid - 1
            else:
                return new_mid
        return -1
        