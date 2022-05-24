
from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        x = n // 2
        piv = -1
        #print(f'nums:{nums}')
        if (len(nums) % 2):
            x += 1
        for i in range(x):
            #print(f'{nums[i]}:{nums[n-i-1]}')
            if (nums[i] <= nums[n-i-1]):
                # find pivot here
                if (nums[n-i-1] > nums[(n-i) % n]):
                    piv = i
                else:
                    piv = n-i
                break
        if (piv == -1):
            piv = x
        #print(f'piv:{piv}')

        def bin_search(nums, f, l, target) -> int:
            #print(nums[f:l+1])
            ans = -1
            ln = l-f+1
            if (ln == 1):
                if (target == nums[f]): ans = f;
                return ans
            x = ln // 2 + f
            if (target == nums[x]):
                ans = x
            elif (target > nums[x]):
                ans = bin_search(nums, x, l, target)
            else:
                ans = bin_search(nums, f, x-1, target)
            return ans
        arr = nums[n-piv:]+nums[:n-piv]
        #print(f'arr:{arr}')
        res = bin_search(arr, 0, n-1,  target)
        return (res - piv) % n;

#s = Solution()
#res = s.search([2,3,4,5,1], 1)
#print(res)

class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        print(f'arr:{nums}')
        n = len(nums)
        res = -1
        if (n == 1):
            if (nums[0] == target): res = 0
            return res
        mid = n//2
        if (nums[mid] == target):
            return mid
        elif (nums[0] < nums[mid]):
            # sorted left half
            if (target < nums[mid] and target >= nums[0]):
                res = self.search(nums[0:mid], target)
            else:
                res = self.search(nums[mid:n], target)
                if (res != -1): res += mid
        else:
            # sorted right half
            if (target > nums[mid] and target <= nums[n-1]):
                res = self.search(nums[mid:n], target)
                if (res != -1): res += mid
            else:
                res = self.search(nums[0:mid], target)
        return res

s = Solution2()
arr = [3,4,5,1,2]
trgt = 5
res = s.search(arr, trgt)
print(f'arr:{arr} target:{trgt} res:{res}')

#x=[3,4,5,1,2]
#x1 = x[3:]+x[:3]
#print(x1)