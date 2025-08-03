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
        # Binary search
        st = 0
        end = len(nums)-1
        res = -1

        while (st <= end):
            mid = st + ((end - st) // 2)
            if (nums[mid] == target):
                res = mid
                break
            elif (target < nums[mid]):
                end = mid - 1
            else:
                st = mid + 1
        return res        

s = Solution()

nums = []
res = s.Search(nums, 3)
print(f'arr:{nums} res:{res}')
