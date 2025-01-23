class Solution:
    """
    Time complexity: O(n) -> 2 * O(n)
    Space complexity: O(n) for the result array
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix, suffix = 1, 1
        result = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix *= nums[i-1]
            result[i] = prefix

        for i in range(len(nums) - 2, -1, -1):
            suffix *= nums[i+1]
            result[i] *= suffix

        return result