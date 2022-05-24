'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
'''
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        j = n
        for i in range(n):
            if (nums[i] == 0):
                j = i
                break

        l,r = j,j
        while (r < n):
            if (nums[r] != 0):
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
            r += 1
        
s = Solution()
nums = [1,0,0,2,3,4,0,9]
print(f'nums:{nums}')
s.moveZeroes(nums)
print(f'moved:{nums}')
