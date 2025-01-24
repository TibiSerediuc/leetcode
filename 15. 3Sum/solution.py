class Solution:
    """
    Time complexity:  O(n^2) -> O(nlogn) for sorting + O(n^2) for finding the 3 elements
    Space complexity: O(1)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                totalSum = nums[i] + nums[l] + nums[r]

                if totalSum > 0:
                    r -= 1
                elif totalSum < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

        return result