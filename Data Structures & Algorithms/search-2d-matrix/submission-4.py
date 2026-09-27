class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        i, j = 0, rows * cols - 1

        while i <= j :
            mid = i + (j - i) // 2

            if target > matrix[mid // cols][mid % cols]:
                i = mid + 1
            elif target < matrix[mid // cols][mid % cols]:
                j = mid - 1
            else:
                return True
        return False

        # exploded = []
        # for m in matrix:
        #     exploded.extend(m)
        # print(exploded)
        # i = 0
        # j = len(exploded) - 1
        # while i <= j:
        #     mid = i + (j-i)//2

        #     if target > exploded[mid]:
        #         i = mid + 1
        #     elif target < exploded[mid]:
        #         j = mid - 1
        #     else:
        #         return True
        # return False


            
                
