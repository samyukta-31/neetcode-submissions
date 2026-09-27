class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        exploded = []
        for m in matrix:
            exploded.extend(m)
        print(exploded)
        i = 0
        j = len(exploded) - 1
        while i <= j:
            mid = i + (j-i)//2

            if target > exploded[mid]:
                i = mid + 1
            elif target < exploded[mid]:
                j = mid - 1
            else:
                return True
        return False


            
                
