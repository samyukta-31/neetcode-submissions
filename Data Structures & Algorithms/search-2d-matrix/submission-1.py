class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for elem in matrix:
            low = 0
            high = len(elem) - 1
            if target > elem[-1]:
                continue
            while low <= high:
                mid = (low+high)//2
                if elem[mid] > target:
                    high = mid - 1
                elif elem[mid] < target:
                    low = mid + 1
                else:
                    return True
        return False


            
                
