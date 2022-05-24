from typing import List

'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''


class Solution:
    def Search(self, nums: List[int], target: int) -> int:
        ln = len(nums)
        if (ln == 0): return -1
        if (ln == 1 and target == nums[0]):
            return 0
        elif (ln == 1): return -1

        mid = ln // 2
        if (nums[mid] == target):
            return mid
        elif (target < nums[mid]):
            return self.Search(nums[:mid], target)
        else:
            res = self.Search(nums[mid:], target)
            return res if res == -1 else mid + res

s = Solution()

nums = []
res = s.Search(nums, 3)
print(f'arr:{nums} res:{res}')
