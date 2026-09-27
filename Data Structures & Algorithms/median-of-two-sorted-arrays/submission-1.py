class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i1 = 0
        i2 = 0
        j1 = len(nums1)
        j2 = len(nums2)
        median_indices = [(j1+j2)//2] if (j1+j2)%2 !=0 else [(j1+j2)//2, ((j1+j2)//2) - 1]
        count = 0
        to_append = None

        for _ in range(0, j1 + j2):
            if count == median_indices[0]:
                prev_append = to_append
            if i1 == j1:
                to_append = nums2[i2]
                i2 += 1
            elif i2 == j2:
                to_append = nums1[i1]
                i1 += 1
            elif nums1[i1] <= nums2[i2]:
                to_append = nums1[i1]
                i1 += 1
            else:
                to_append = nums2[i2]
                i2 += 1
            if count == median_indices[0]:
                if len(median_indices) == 2:
                    return (prev_append + to_append)/2
                else:
                    return to_append
            count += 1

