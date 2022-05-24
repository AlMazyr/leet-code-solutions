from typing import List

class Solution:
    def findRowNum(self, matrix: List[List[int]], target: int) -> int:        
        n = len(matrix)
        res = -1
        if (n == 1):
            if (target >= matrix[0][0] and target <= matrix[0][-1]): res = 0
            return res

        mid = n//2
        if (target >= matrix[mid][0] and target <= matrix[mid][-1]):
            res = mid
        elif (target < matrix[mid][0]):
            res = self.findRowNum(matrix[0:mid], target)
        else: # target > matrix[mid][-1]
            res = self.findRowNum(matrix[mid:], target)
            if (res != -1): res += mid
        return res

    def binSearch(self, array: List[int], target: int) -> bool:
        n = len(array)
        res = False
        if (n == 1):
            if (target == array[0]): res = True
            return res
        
        mid = n//2
        if (target == array[mid]):
            res = True
        elif (target < array[mid]):
            res = self.binSearch(array[:mid], target)
        else:
            res = self.binSearch(array[mid:], target)
        return res

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = False
        row = self.findRowNum(matrix, target)
        if (row != -1): res = self.binSearch(matrix[row], target) 
        return res

mtrx = [[1,2,3], [4,5,6], [8,9,10]]
trgt = 6
s = Solution()
#print(s.findRowNum(mtrx, 2))
#print(s.binSearch(mtrx[1], trgt))
print(s.searchMatrix(mtrx, trgt))