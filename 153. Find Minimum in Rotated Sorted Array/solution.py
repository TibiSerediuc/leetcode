class Solution:
    """
    Time complexity: O(logn)
    Space complexityL O(1)
    """
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:

            mid = (l + r) // 2
            res = min(res, nums[mid])
            #if the subarray is sorted we return the first value
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            elif nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return res