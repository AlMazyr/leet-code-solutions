'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.
'''

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Make squares
        res = [x*x for x in nums]

        # Find l and r
        prev = res[0]+1
        n = len(res)
        l = n-1
        r = n
        print(f'prev={prev} n={n}')
        for i in range(n):
            if (res[i] > prev):
                r = i
                l = i-1
                break
            prev = res[i]
        print(f'l={l} r={r}')

        # Sort array
        res1 = []
        while (l >= 0 and r <= (n-1)):
            if (res[l] <= res[r]):
                res1 += [res[l]]
                l -= 1
            else:
                res1 += [res[r]]
                r += 1
        print(f'l={l} r={r} res1={res1}')

        # Copy tail here
        while (l >= 0):
            res1 += [res[l]]
            l -= 1
        while (r <= (n-1)):
            res1 += [res[r]]
            r += 1

        return res1

s = Solution()
nums = [-4,-4,-3]
res=s.sortedSquares(nums)
print(f'nums={nums} res={res}')
