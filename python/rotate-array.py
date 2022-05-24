'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''
from copy import copy
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            j = (i + k) % n
            res[j] = nums[i]
        for i in range(n):
            nums[i] = res[i]
    
    def reverse(self, nums: List[int], l: int, r: int) -> None:
        while(l < r):
            nums[l],nums[r] = nums[r],nums[l]     
            l += 1
            r -= 1

    def rotate_in_place(self, nums: List[int], k: int) -> None:
        n = len(nums)
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)

s = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
print(f'Intput: nums:{nums} k:{k}')
#s.rotate(nums, k)
#print(f'nums={nums} k={k}')
#s.reverse(nums)
#print(f'reverse={nums}')
s.rotate_in_place(nums, k)
print(f'rotated={nums}')