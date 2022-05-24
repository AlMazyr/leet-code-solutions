'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary search
        st = 0
        end = len(nums)-1
        #res = -1

        while (st <= end):
            mid = st + ((end - st) // 2)
            if (nums[mid] == target):
                st = mid
                break
            elif (target < nums[mid]):
                end = mid - 1
            else:
                st = mid + 1

        return st        



s = Solution()

nums = [1,3,5,7]
target = 6

res = s.searchInsert(nums, target)
print(f'nums={nums} target={target} res = {res}')